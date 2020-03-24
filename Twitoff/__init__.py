# Web_App/Twitoff/__init__.py

from flask import Flask

from Twitoff.routes.home_routes import home_routes
from Twitoff.routes.book_routes import book_routes
from Twitoff.models import db, migrate

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\ricci\\Google Drive\\Colab Notebooks\\Unit_3\\Sprint_3\\Web_App\\Twitoff.db"


    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)