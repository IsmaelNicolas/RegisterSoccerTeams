from flask import Flask
from config import config
from flask_cors import CORS

# ROUTES
from routes import Team
from routes import Category
from routes import Player

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "http://localhost:3000"}})


def page_not_found(error):
    return " ", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BLUEPIRNTS
    app.register_blueprint(Team.main, url_prefix='/api/teams')
    app.register_blueprint(Category.main, url_prefix='/api/categories')
    app.register_blueprint(Player.main, url_prefix='/api/players')


    # ERROR HANDLRES
    app.register_error_handler(404, page_not_found)

    # RUNNING SERVER
    app.run()
