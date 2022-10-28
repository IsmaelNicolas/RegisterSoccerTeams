from unicodedata import category


class Player():

    def __init__(self, playerCode =None, playerName=None, playerNumber=None, playerAge=None, playerPossition=None,
    categoryCode =None , teamCode =None ) -> None:
        
        self.playerCode  = playerCode
        self.playerName = playerName
        self.playerNumber =  playerNumber 
        self.playerAge = playerAge 
        self.playerPossition = playerPossition
        self.categoryCode = categoryCode
        self.teamCode = teamCode

    def to_JSON(self):
        return {
            'playerCode'  : self.playerCode,
            'categoryCode' : self.categoryCode,
            'teamCode' : self.teamCode,
            'playerName' : self.playerName,
            'playerNumber' :  self.playerNumber, 
            'playerAge' : self.playerAge ,
            'playerPossition' : self.playerPossition
        }