from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!, this is my first Python Application"

@application.route("/hello")
def helloTest():
    return "Hello World!, this is my first Python Application in Docker"

if __name__ == "__main__":
    application.run()
