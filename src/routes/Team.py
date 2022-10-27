from flask import Blueprint, jsonify,request

#ENTITIES
from models.entities.Team import Team
# MODELS
from models.TeamModel import TeamModel

main = Blueprint('teams_blueprint', __name__)


@main.route('/')
def get_teams():

    try:
        teams = TeamModel.get_teams()
        return jsonify(teams), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/<id>')
def get_team(id):

    try:
        team = TeamModel.get_team(id)
        if team != None:
            return jsonify(team), 200
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/add',methods=['POST'])
def add_team():

    try:
        categoryCode = request.json['categoryCode']
        teamCoach = request.json['teamCoach']
        teamName =request.json['teamName']

        team = Team(categoryCode= categoryCode, teamCoach = teamCoach , teamName=teamName)
     
        affectedRows = TeamModel.add_team(team=team)

        if affectedRows == 1:
            return ({'message':'correct insertion'})
        else:
            raise Exception('could not be inserted')

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/delete/<id>',methods=['DELETE'])
def delete_team(id):

    try:
             
        affectedRows = TeamModel.delete_team(id)

        if affectedRows == 1:
            return ({'message':'successfully eliminated'})
        else:
            raise Exception('could not be removed')

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/update/<id>',methods=['PUT'])
def update_team(id):

    try:
        categoryCode = request.json['categoryCode']
        teamCoach = request.json['teamCoach']
        teamName =request.json['teamName']

        team = Team(teamCode=id ,categoryCode= categoryCode, teamCoach = teamCoach , teamName=teamName)
             
        affectedRows = TeamModel.update_team(team=team)

        if affectedRows == 1:
            return ({'message':'correct update'})
        else:
            raise Exception('could not be updated')

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500