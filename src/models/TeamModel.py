from multiprocessing import connection
from database.db import get_connection
from .entities.Team import Team


class TeamModel():

    @classmethod
    def get_teams(self):
        try:
            query = 'SELECT teamCode,teamName,teamCoach FROM team;'
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute(query=query)
                resultset = cursor.fetchall()

                for row in resultset:
                    team = Team(row[0],row[1],row[2])     
                    teams.append(team.to_JSON()) 
            connection.close()
            return teams

        except Exception as ex:
            raise Exception(ex)
