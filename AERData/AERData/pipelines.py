import psycopg2
from .items import Problem, User, Category


class AerdataPipeline(object):

    # Process and manage the item when it was scrapped from the database
    def process_item(self, item, spider):

        # Some if to manage the data according to Object type
        if isinstance(item, Problem):
            try:
                # Insert problems on database or updated if exist
                query = "INSERT INTO problems(id_problem,title,no_repeated_accepteds," \
                        "wrong_answer,accepteds,shipments,time_limit,memory_limit,presentation_error," \
                        "attempts,other,restricted_function,compilation_error,c_shipments,cpp_shipments," \
                        "java_shipments, category_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" \
                        "ON CONFLICT (id_problem) DO UPDATE SET id_problem = %s,title = %s,no_repeated_accepteds = %s," \
                        "wrong_answer = %s,accepteds = %s,shipments = %s,time_limit = %s,memory_limit = %s," \
                        "presentation_error = %s, attempts = %s,other = %s,restricted_function = %s,compilation_error = %s," \
                        "c_shipments = %s,cpp_shipments = %s, java_shipments = %s, category_id = %s"
                # values for query
                values = (
                    item["number"], item["title"], item["no_repeated_accepteds"], item["wrong_answer"],
                    item["accepteds"], item["shipments"], item["time_limit"], item["memory_limit"],
                    item["presentation_error"], item["attempts"], item["other"], item["restricted_function"],
                    item["compilation_error"], item["c_shipments"], item["cpp_shipments"], item["java_shipments"],
                    item["category"], item["number"], item["title"], item["no_repeated_accepteds"],
                    item["wrong_answer"],
                    item["accepteds"], item["shipments"], item["time_limit"], item["memory_limit"],
                    item["presentation_error"], item["attempts"], item["other"], item["restricted_function"],
                    item["compilation_error"], item["c_shipments"], item["cpp_shipments"], item["java_shipments"],
                    item["category"])

                # execute and commit
                self.cur.execute(query, values)
                self.connection.commit()

                return item
            except Exception as e:
                print("Fallo insertando Problemas")
                print(e)
        # Some if to manage the data according to Object type
        elif isinstance(item, User):
            try:
                # Todo Gestionar usuarios
                print("a")
            except Exception as e:
                print("Fallo insertando usuarios")
                print(e)
        # Some if to manage the data according to Object type
        elif isinstance(item, Category):
            try:
                # Insert problems on database or updated if exist
                query = "INSERT INTO categories(id_category,name,related_category) VALUES (%s,%s,%s)" \
                        "ON CONFLICT (id_category) DO UPDATE SET id_category = %s, name = %s, related_category = %s"

                # Values for query
                values = (
                    item['id'], item['name'], item['related_category'],
                    item['id'], item['name'], item['related_category'])

                self.cur.execute(query, values)
                self.connection.commit()
                return item
            except Exception as e:
                print("Fallo insertando categorias")
                print(e)
        else:
            return item

    # Define function to connect to database
    def open_spider(self, spider):
        hostname = 'postgresql'
        username = 'root'
        password = 'example'
        database = 'API_AER'
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password,
            dbname=database)
        self.cur = self.connection.cursor()

    # Define function to disconnect from database
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()
