from flask import jsonify

from server import db
from ..models.dish import (
    Dish,
    DishSchema,
    CreateDishSchema,
    UpdateDishSchema
)


def all_dishes():
    dish_schema = DishSchema(many=True)
    dishes = Dish.query.all()
    response = dish_schema.dump(dishes)
    return jsonify(response), 200


def get_a_dish(dish_id):
    dish = Dish.query.get(dish_id)
    if dish:
        dish_schema = DishSchema()
        response = dish_schema.dump(dish), 200
    else:
        response = jsonify('Dish not found'), 404
    return response


def create_dish(data):
    create_dish_schema = CreateDishSchema()
    errors = create_dish_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    dish = Dish.query.filter_by(name=data['name']).first()
    if not dish:
        dish = Dish(
            name=data['name'],
            description=data['description'],
            country=data['country'],
            category=data['category']
        )
        _save_dish(dish)
        dish_schema = DishSchema()
        response = dish_schema.dump(dish), 201
    else:
        response = jsonify('Dish already exists'), 409
    return response


def update_dish(data, dish_id):
    update_dish_schema = UpdateDishSchema()
    errors = update_dish_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    dish = Dish.query.get(dish_id)
    if dish:
        check_for_update = ['description', 'country', 'category']
        for field in check_for_update:
            if data.get(field):
                setattr(dish, field, data[field])
        _save_dish(dish)
        response = jsonify('Dish sucessfully updated'), 200
    else:
        response = jsonify('Dish not found'), 404
    return response


def delete_a_dish(dish_id):
    dish = Dish.query.get(dish_id)
    if dish:
        db.session.delete(dish)
        db.session.commit()
        response = jsonify('Dish deleted'), 200
    else:
        response = jsonify('Dish not found'), 404
    return response


def _save_dish(dish):
    db.session.add(dish)
    db.session.commit()
