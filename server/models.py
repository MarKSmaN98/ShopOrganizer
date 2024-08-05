from sqlalchemy_serializer import SerializerMixin

from config import db
from datetime import datetime

class Tech(db.Model, SerializerMixin):
    __tablename__ = "techs"
    serialize_rules = ("tech_cars", "-tech_cars.tech", )

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    rate = db.Column(db.Float)

    tech_cars = db.relationship('Car', backref = 'tech', cascade='all, delete')

class Car(db.Model, SerializerMixin):
    __tablename__ = 'cars'
    serialize_rules = ("tech", "-parts.car", "-notes.car", "-images.car", )

    id = db.Column(db.Integer, primary_key = True)
    inDate = db.Column(db.DateTime, default = datetime.now)
    year = db.Column(db.Integer)
    make = db.Column(db.String)
    model = db.Column(db.String)
    owner = db.Column(db.String)
    stage = db.Column(db.Integer, default=0)

    tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'))
    parts = db.relationship('Part', backref = 'car', cascade = 'all, delete')
    notes = db.relationship('Note', backref = 'car', cascade = 'all, delete')
    images = db.relationship('Image', backref = 'car', cascade = 'all, delete')

class Part(db.Model, SerializerMixin):
    __tablename__ = 'parts'
    serialize_rules = ("car.id",)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    hours = db.Column(db.Float)

    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))


class Note(db.Model, SerializerMixin):
    __tablename__ = 'notes'
    serialize_rules = ("car.id", "tech_id", )

    id = db.Column(db.Integer, primary_key = True)
    created = db.Column(db.DateTime, default=datetime.now)
    note = db.Column(db.String)\
    
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
    tech_id = db.Column(db.Integer, db.ForeignKey('techs.id'))

class Image(db.Model, SerializerMixin):
    __tablename__ = 'images'
    serialize_rules = ("car.id", )

    id = db.Column(db.Integer, primary_key = True)

    img = db.Column(db.String)
    date = db.Column(db.DateTime, default = datetime.now)

    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))
