from marshmallow import Schema, fields

from server import db, ma


class Dish(db.Model):
    __tablename__ = 'dishes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, unique=True)
    description = db.Column(db.String(120), index=True, nullable=False)
    country = db.Column(db.String(120), index=True, nullable=False)
    category = db.Column(db.String(120), index=True, nullable=False)


class DishSchema(ma.ModelSchema):
    class Meta:
        model = Dish


class CreateDishSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    country = fields.Str(required=True)
    category = fields.Str(required=True)


class UpdateDishSchema(Schema):
    description = fields.Str(required=False)
    country = fields.Str(required=False)
    category = fields.Str(required=False)
