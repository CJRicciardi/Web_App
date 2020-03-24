# Web_App/Twitoff/__init__.py

from flask import Flask

#from twitoff.routes.home_routes import home_routes
#from twitoff.routes.book_routes import book_routes


def create_app():
    app = Flask(__name__)
    #app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)

    @app.route("/")
    def hello():
        print('vsited the hello page')
        return "Hello World!"

    @app.route("/about")
    def about():
        print('visited the about page')
        return "About me"

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)