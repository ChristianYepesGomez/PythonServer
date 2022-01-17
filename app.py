from flask import Flask

print("a")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
