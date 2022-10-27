from database.db import get_connection
from .entities.Team import Team


class TeamModel():

    @classmethod
    def get_teams(self):
        try:
            query = 'SELECT teamCode,teamName,teamCoach,categoryCode FROM team;'
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute(query=query)
                resultset = cursor.fetchall()

                for row in resultset:
                    team = Team(row[0], row[1], row[2], row[3])
                    teams.append(team.to_JSON())
            connection.close()
            return teams

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_team(self, id):
        try:
            query = "SELECT teamCode,teamName,teamCoach,categoryCode FROM team WHERE teamCode = %s;"
            connection = get_connection()
            teams = []

            with connection.cursor() as cursor:
                cursor.execute(query, (id,))
                row = cursor.fetchone()

                team = None
                if row != None:
                    team = Team(row[0], row[1], row[2], row[3])
                    team = team.to_JSON()

            connection.close()
            return team

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_team(self, team):
        try:
 
            query = "INSERT INTO team (categorycode, teamname, teamcoach) VALUES (%s,%s,%s)"
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(query, (team.categoryCode,
                               team.teamName, team.teamCoach))

                affectedRows = cursor.rowcount
                connection.commit()

            connection.close()
            return affectedRows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_team(self, id):
        try:
            
            query = "DELETE FROM team WHERE teamCode = %s"
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(query, (id,))

                affectedRows = cursor.rowcount
                connection.commit()

            connection.close()
            return affectedRows

        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_team(self, team):
        try:
 
            query = "UPDATE team SET teamName = %s, teamCoach = %s , categoryCode = %s WHERE teamCode = %s"
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(query, (team.teamName , team.teamCoach, team.categoryCode, team.teamCode))

                affectedRows = cursor.rowcount
                connection.commit()

            connection.close()
            return affectedRows

        except Exception as ex:
            raise Exception(ex)