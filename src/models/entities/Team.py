class Team():
     
    def __init__(self, teamCode = None, teamName=None, teamCoach=None,categoryCode=None):
        self.teamCode = teamCode
        self.teamName = teamName
        self.teamCoach = teamCoach
        self.categoryCode = categoryCode

    def to_JSON(self):
        return {
            'teamCode':self.teamCode, 
            'teamName':self.teamName, 
            'teamCoach':self.teamCoach,
            'categoryCode':self.categoryCode
        }