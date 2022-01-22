# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Class Problem to scrap data from webpage and save it
class Problem(scrapy.Item):
    price = scrapy.Field()
    # General data from the problem
    number = scrapy.Field()
    title = scrapy.Field()
    accepteds = scrapy.Field()
    no_repeated_accepteds = scrapy.Field()
    wrong_answer = scrapy.Field()
    time_limit = scrapy.Field()
    memory_limit = scrapy.Field()
    presentation_error = scrapy.Field()
    shipments = scrapy.Field()
    attempts = scrapy.Field()
    other = scrapy.Field()
    restricted_function = scrapy.Field()
    run_time_error = scrapy.Field()
    compilation_error = scrapy.Field()
    c_shipments = scrapy.Field()
    cpp_shipments = scrapy.Field()
    java_shipments = scrapy.Field()
    category = scrapy.Field()


# Class User to scrap data from webpage and save it
class User(scrapy.Item):
    nick = scrapy.Field()
    name = scrapy.Field()
    country = scrapy.Field()
    institution = scrapy.Field()
    logo_src = scrapy.Field()
    shipments = scrapy.Field()
    total_accepteds = scrapy.Field()
    intents = scrapy.Field()
    accepteds = scrapy.Field()


# Class Category to scrap data from webpage and save it
class Category(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    related_category = scrapy.Field()
