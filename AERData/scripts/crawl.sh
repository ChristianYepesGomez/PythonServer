#!/bin/sh
echo "Running"
# go to the spider directory
cd /app/AERData/AERData/
PATH=$PATH:/usr/local/bin
export PATH
# run the spider
scrapy crawl AERProblems
scrapy crawl AERProblemsByCategory
scrapy crawl AERCategories
scrapy crawl AERUsers