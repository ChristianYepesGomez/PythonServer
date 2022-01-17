from flask import Flask

app = Flask(__name__)
import os

os.system('cmd /c "scrapy crawl AERProblems"')


@app.route('/')
def hello_world():
    return 'Hello, Docker!'
