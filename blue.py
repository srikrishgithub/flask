from flask import Flask
from admin import order_manager_blueprint

site = Flask(__name__)
site.register_blueprint(blueprint)


@site.route("/")
def admin():
    return "<h1>This is the admin page</h1>"

if __name__ == '__main__':
   site.run()



# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return "Hello, This is home page."

# if __name__ == '__main__':
#    app.run()