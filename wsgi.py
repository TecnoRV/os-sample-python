from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World this is my first OpenShift Demo V2"

if __name__ == "__main__":
    application.run()
