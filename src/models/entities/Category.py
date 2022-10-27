class Category():

    def __init__(self, categoryCode, categoryName=None, categoryMinAge=None, categoryMaxAge=None) -> None:

        self.categoryCode = categoryCode
        self.categoryName = categoryName
        self.categoryMinAge = categoryMinAge
        self.categoryMaxAge = categoryMaxAge

    def to_JSON(self):

        return {
            'categoryCode': self.categoryCode,
            'categoryName': self.categoryName,
            'categoryMinAge': self.categoryMinAge,
            'categoryMaxAge': self.categoryMaxAge,

        }
