from multiprocessing import connection
from unicodedata import category
from database.db import get_connection
from .entities.Category import Category


class CategoryModel():

    @classmethod
    def get_category(self):
        try:
            query = "SELECT categorycode, categoryname, categoryminage, categorymaxage FROM category;"
            connection = get_connection()

            categories = []

            with connection.cursor() as cursor:
                cursor.execute(query=query)
                resultset = cursor.fetchall()

                for row in resultset:
                    category = Category(categoryCode=row[0],
                                        categoryName=row[1],
                                        categoryMinAge=row[2],
                                        categoryMaxAge=row[3])
                    categories.append(category.to_JSON())

            return categories

        except Exception as ex:
            raise Exception(ex)
