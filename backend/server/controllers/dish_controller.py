from flask import Blueprint
from flask import request
from flask_cors import CORS

from ..services.dish_service import (
    all_dishes,
    get_a_dish,
    create_dish,
    update_dish,
    delete_a_dish
)

dishes = Blueprint('dishes', __name__, url_prefix='/api/dishes')
CORS(dishes, max_age=30 * 86400)


@dishes.route('/', methods=['GET'])
def get_all_dishes():
    """
    .. http:get:: /api/dishes/

    Function that returns all the dishes.

    :returns: The dishes.
    :rtype: list.
    """
    return all_dishes()


@dishes.route('/<int:dish_id>', methods=['GET'])
def get_dish(dish_id):
    """
    .. http:get:: /api/dishes/(int:dish_id)

    Function that given an id it returns the dish.

    :param dish_id: the id of the dish.
    :type dish_id: int

    :returns: The dish
    :rtype: Dish

    """
    return get_a_dish(dish_id)


@dishes.route('', methods=['POST'])
def post_dish():
    """
    .. http:post:: /api/dishes

    Function that given the dish data it creates it.

    Example::

        body = {
            'name': 'The dish name',
            'description': 'The dish description',
            'country': 'A country',
            'category': 'The category'
        }

    :param body: the data of the dish sent in the body of the request.
    :type body: dict

    """
    data = request.get_json()
    return create_dish(data)


@dishes.route('/<int:dish_id>', methods=['PUT'])
def put_dish(dish_id):
    """
    .. http:put:: /api/dishes/(int:dish_id)

    Function that given the dish_id it updates it with the data sent in the
    body of the request.

    Example::

        body = {
            'description': 'The dish description',
            'country': 'A country',
            'category': 'The category'
        }

    :param dish_id: the id of the dish.
    :type dish_id: int
    :param body: the data of the dish sent in the body of the request.
    :type body: dict
    """
    data = request.get_json()
    return update_dish(data, dish_id)


@dishes.route('/<int:dish_id>', methods=['DELETE'])
def delete_dish(dish_id):
    """
    .. http:delete:: /api/dishes/(int:dish_id)

    Function that given the dish id it deletes it.

    :param dish_id: the id of the dish.
    :type dish_id: int
    """
    return delete_a_dish(dish_id)
