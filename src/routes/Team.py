from flask import Blueprint, jsonify

# MODELS
from models.TeamModel import TeamModel

main = Blueprint('soocer_blueprint', __name__)


@main.route('/')
def get_teams():

    try:
        teams = TeamModel.get_teams()
        return jsonify(teams), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
