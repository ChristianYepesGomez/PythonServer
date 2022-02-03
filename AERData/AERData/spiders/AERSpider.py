from ..items import *

# Blacklist with the ID of the users that doesn't exist
users_blacklist = []


# Get Problems class
class Problems(scrapy.Spider):
    name = 'AERProblems'
    start_urls = ['https://www.aceptaelreto.com']

    def parse(self, response):
        # Scrap volumes XML
        yield scrapy.Request(url='https://www.aceptaelreto.com/ws/volume',
                             callback=self.create_problems_url)

    def create_problems_url(self, response):
        # Get ids from volumes
        volume = response.xpath('//id/text()')

        # For every volumeID then scrap XML with problems
        for id in volume:
            url_problemas = 'https://www.aceptaelreto.com/ws/volume/{}/problems/?_=1642276528309'.format(id.get())

            yield scrapy.Request(url=url_problemas, callback=self.parse_problema)

    def parse_problema(self, response):

        problems = response.xpath("//problem")
        for problem in problems:
            # Create item for every problem
            problem_item = Problem()
            # General data from the problem
            problem_item['number'] = problem.xpath('.//num/text()').get()
            problem_item['title'] = problem.xpath('.//title/text()').get()
            # Stadistic data from the problem
            problem_item['accepteds'] = problem.xpath('.//ac/text()').get()
            problem_item['no_repeated_accepteds'] = problem.xpath('.//dacu/text()').get()
            problem_item['wrong_answer'] = problem.xpath('.//wa/text()').get()
            problem_item['time_limit'] = problem.xpath('.//tl/text()').get()
            problem_item['memory_limit'] = problem.xpath('.//ml/text()').get()
            problem_item['presentation_error'] = problem.xpath('.//pe/text()').get()
            problem_item['shipments'] = problem.xpath('.//totalSubs/text()').get()
            problem_item['attempts'] = problem.xpath('.//totalUsers/text()').get()
            problem_item['other'] = problem.xpath('.//ol/text()').get()
            problem_item['restricted_function'] = problem.xpath('.//rf/text()').get()
            problem_item['run_time_error'] = problem.xpath('.//rte/text()').get()
            problem_item['compilation_error'] = problem.xpath('.//ce/text()').get()
            problem_item['c_shipments'] = problem.xpath('.//c/text()').get()
            problem_item['cpp_shipments'] = problem.xpath('.//cpp/text()').get()
            problem_item['java_shipments'] = problem.xpath('.//java/text()').get()
            problem_item['category'] = None
            yield problem_item


# Get Users class
class Users(scrapy.Spider):
    name = 'AERUsers'
    start_urls = ['https://www.aceptaelreto.com']
    id = 1
    users_failed = 0

    def parse(self, response):
        # when it finds more than 20 users that do not exist stop
        while Users.users_failed < 20:
            # Scrap user info webpage
            yield scrapy.Request(url='https://www.aceptaelreto.com/user/profile.php?id={}'.format(Users.id),
                                 callback=self.parse_user)

    def parse_user(self, response):
        # Generic function to extract data
        def extract_xpath(query):
            return response.xpath('{}/text()'.format(query))

        try:
            # If the user exists, look the info, else go to next
            if not response.xpath("//div[@class='alert alert-danger']"):
                # Check blacklist before try to take info
                if Users.id not in users_blacklist:
                    user = User()
                    user['nick'] = extract_xpath("//div[@class='col-sm-8']//p")[0].get()
                    user['name'] = extract_xpath("//div[@class='col-sm-8']//p")[1].get()
                    user['country'] = extract_xpath("//div[@class='col-sm-8']//p")[2].get().strip()
                    # Try to get the institution and logo, if don't have any use the default text
                    try:
                        user['institution'] = extract_xpath("//div[@class='col-sm-8']//a")[0].get()
                        user['logo_src'] = response.xpath("//div[@class='col-sm-8']//a//img/@src")[0].get(),
                    except:
                        user['institution'] = extract_xpath("//div[@class='col-sm-8']//p")[3].get().strip()
                        user['logo_src'] = ""
                    # If the user have tried to send any solution, look the stats, else set stats to 0
                    if not response.xpath("//div[@class='alert alert-info']"):
                        user['shipments'] = extract_xpath("//div[@class='panel-body text-box text-center']")[
                            0].get().strip()
                        user['total_accepteds'] = extract_xpath("//div[@class='panel-body text-box text-center']")[
                            1].get().strip()
                        user['intents'] = extract_xpath("//div[@class='panel-body text-box text-center']")[
                            2].get().strip()
                        user['accepteds'] = extract_xpath("//div[@class='panel-body text-box text-center']")[
                            3].get().strip()
                    else:
                        user['shipments'] = 0
                        user['total_accepteds'] = 0
                        user['intents'] = 0
                        user['accepteds'] = 0
                    yield user
                    # Reset the failed users
                    Users.users_failed = 0
            else:
                # TODO añadir a la blacklist
                Users.users_failed += 1
        except Exception as e:
            print(e)

        Users.id += 1


# Get Categories
class Categories(scrapy.Spider):
    name = 'AERCategories'
    start_urls = ['https://www.aceptaelreto.com']

    def parse(self, response):
        # Scrap categories the url with all father categories
        yield scrapy.Request(url='https://www.aceptaelreto.com/problems/categories.php',
                             callback=self.parse_category)

    def parse_category(self, response):
        try:
            # Select the text inside <script> from JS file of the webpage
            # and parse it to json with the library chompjs

            import chompjs
            javascript = response.css('script::text').get()
            data = chompjs.parse_js_object(javascript)

            # for each subcategory on the category look if have any child and repeat recursively
            # then check if the category have any problem
            for subcat in data['subcats']:
                # When looking for categories also we do the relation between category and problems
                # and modify the database
                if subcat['numOfProblems'] > 0:
                    yield scrapy.Request(
                        url='https://www.aceptaelreto.com/ws/cat/{}/problems?_=16428085447'.format(subcat['id']),
                        callback=self.parse_problem_category)
                else:
                    yield scrapy.Request(
                        url='https://www.aceptaelreto.com/problems/categories.php/?cat={}'.format(subcat['id']),
                        callback=self.parse_category)

            # Create a Category object to save the data
            category_object = Category()
            # Need the index to the relation between categories
            index = len(data['path'])

            # Relation between the Category object and the scrapped data
            category_object['id'] = data['id']
            category_object['name'] = data['name']

            # If have some path, have a relation
            if (index == 0):
                category_object['related_category'] = None
                yield category_object
            else:
                # The relation its calculated with the last item in the 'path' and his ID
                category_object['related_category'] = data['path'][int(index) - 1]['id']

            # Call pipelines to manage the object
            yield category_object

        except Exception as e:
            print("La categoria no existe")
            print(e)

    def parse_problem_category(self, response):
        # Get problems list
        problems_list = response.xpath('//problem')

        # With this list we have the ID of the category on de url so we can relate Problems and Category
        # --> Can't use only the scrap of the problems because not all problems have a category <--

        for problem in problems_list:
            # Create item for every problem
            problem_item = Problem()
            # General data from the problem
            problem_item['number'] = problem.xpath('.//num/text()').get()
            problem_item['title'] = problem.xpath('.//title/text()').get()
            # Stadistic data from the problem
            problem_item['accepteds'] = problem.xpath('.//ac/text()').get()
            problem_item['no_repeated_accepteds'] = problem.xpath('.//dacu/text()').get()
            problem_item['wrong_answer'] = problem.xpath('.//wa/text()').get()
            problem_item['time_limit'] = problem.xpath('.//tl/text()').get()
            problem_item['memory_limit'] = problem.xpath('.//ml/text()').get()
            problem_item['presentation_error'] = problem.xpath('.//pe/text()').get()
            problem_item['shipments'] = problem.xpath('.//totalSubs/text()').get()
            problem_item['attempts'] = problem.xpath('.//totalUsers/text()').get()
            problem_item['other'] = problem.xpath('.//ol/text()').get()
            problem_item['restricted_function'] = problem.xpath('.//rf/text()').get()
            problem_item['run_time_error'] = problem.xpath('.//rte/text()').get()
            problem_item['compilation_error'] = problem.xpath('.//ce/text()').get()
            problem_item['c_shipments'] = problem.xpath('.//c/text()').get()
            problem_item['cpp_shipments'] = problem.xpath('.//cpp/text()').get()
            problem_item['java_shipments'] = problem.xpath('.//java/text()').get()
            problem_item['category'] = response.url.split("/")[5]
            yield problem_item
