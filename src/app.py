from flask import Flask
from config import config
from flask_cors import CORS

# ROUTES
from routes import Team

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost"} })


def page_not_found(error):
    return " ", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BLUEPIRNTS
    app.register_blueprint(Team.main, url_prefix='/api/teams')

    # ERROR HANDLRES
    app.register_error_handler(404, page_not_found)

    # RUNNING SERVER
    app.run()
