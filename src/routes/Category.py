from flask import Blueprint, jsonify,request

#ENTITIES
from models.entities.Category import Category
#MODELS
from models.CategoryModel import CategoryModel

main = Blueprint('categories_blueprint', __name__)

@main.route('/')
def get_categories():

    try:
        categories = CategoryModel.get_category()
        return jsonify(categories), 200
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500