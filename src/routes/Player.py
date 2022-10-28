from flask import Blueprint, jsonify,request

from models.entities.Player import Player
from models.PlayerModel import PlayerModel

main = Blueprint('players_blueprint', __name__)


@main.route('/')
def get_teams():

    try:
        players = PlayerModel.get_players()
        return jsonify(players), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500