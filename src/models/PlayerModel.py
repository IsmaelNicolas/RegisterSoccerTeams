from database.db import get_connection
from .entities.Player import Player


class PlayerModel():

    @classmethod
    def get_players(self):
        try:
            query = 'SELECT playercode, categorycode, teamcode, playername, playernumber, playerage, playerpossition FROM public.player;'
            connection = get_connection()
            players = []

            with connection.cursor() as cursor:
                cursor.execute(query=query)
                resultset = cursor.fetchall()

                for row in resultset:
                    player = Player(playerCode=row[0],
                                    categoryCode=row[1], teamCode=row[2],
                                    playerName=row[3], playerNumber=row[4],
                                    playerAge=row[5],
                                    playerPossition=row[6]
                                    )
                    players.append(player.to_JSON())
            connection.close()
            return players

        except Exception as ex:
            raise Exception(ex)
