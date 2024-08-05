from flask import request, make_response, jsonify
from flask_restful import Resource

from config import app, db, api
from models import Tech, Car, Image, Note, Part


class GetTechs(Resource):
    def get(self):
        techList = []
        for tech in Tech.query.all():
            techList.append(tech.to_dict())
        return make_response(techList, 200)
    
    def post(self):
        new = Tech(
            name = request.get_json()['name'],
            rate = request.get_json()['rate'],
        )
        try:
            db.session.add(new)
            db.session.commit()
            return make_response(new.to_dict(), 200)
        except:
            return make_response({'error': 'Cannot add tech'}, 400)
api.add_resource(GetTechs, '/techs')

class GetTechbyId(Resource):
    def get(self, id):
        target = Tech.query.filter(Tech.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find tech'}, 404)
        else:
            return make_response(target.to_dict(), 200)
    
    def patch(self, id):
        target = Tech.query.filter(Tech.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find tech'}, 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(target, attr, data[attr])
            try: 
                db.session.add(target)
                db.session.commit()
                return make_response(target.to_dict(), 200)
            except:
                make_response({"error":"Cannot edit tech"}, 400)

    def delete(self, id):
        target = Tech.query.filter(Tech.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find tech'}, 404)
        else:
            try:
                db.session.delete(target)
                db.session.commit()
                return make_response({}, 204)
            except:
                return make_response({"error":"Cannot delete Tech"}, 400)
api.add_resource(GetTechbyId, '/tech/<int:id>')

class GetCars(Resource):
    def get(self):
        carList = []
        for car in Car.query.all():
            carList.append(car.to_dict())
        return make_response(carList, 200)
    
    def post(self):
        new = Car(
            year = request.get_json()['year'],
            make = request.get_json()['make'],
            model = request.get_json()['model'],
            stage = request.get_json()['stage'],
            owner = request.get_json()['owner'],
            tech_id = request.get_json()['techid'],
        )
        try:
            db.session.add(new)
            db.session.commit()
            return make_response(new.to_dict(), 200)
        except:
            return make_response({'error': 'Cannot add car'}, 400)
api.add_resource(GetCars, '/cars')

class GetCarbyId(Resource):
    def get(self, id):
        target = Car.query.filter(Car.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find car'}, 404)
        else:
            return make_response(target.to_dict(), 200)
    
    def patch(self, id):
        target = Car.query.filter(Car.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find car'}, 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(target, attr, data[attr])
            try: 
                db.session.add(target)
                db.session.commit()
                return make_response(target.to_dict(), 200)
            except:
                make_response({"error":"Cannot edit car"}, 400)

    def delete(self, id):
        target = Car.query.filter(Car.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find car'}, 404)
        else:
            try:
                db.session.delete(target)
                db.session.commit()
                return make_response({}, 204)
            except:
                return make_response({"error":"Cannot delete car"}, 400)
api.add_resource(GetCarbyId, '/car/<int:id>')

class GetParts(Resource):
    def get(self):
        partList = []
        for part in Part.query.all():
            partList.append(part.to_dict())
        return make_response(partList, 200)
    
    def post(self):
        new = Part(
            name = request.get_json()['name'],
            price = request.get_json()['price'],
            hours = request.get_json()['hours'],
            car_id = request.get_json()['carid'],
        )
        try:
            db.session.add(new)
            db.session.commit()
            return make_response(new.to_dict(), 200)
        except:
            return make_response({'error': 'Cannot add part'}, 400)
api.add_resource(GetParts, '/parts')

class GetPartbyId(Resource):
    def get(self, id):
        target = Part.query.filter(Part.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find part'}, 404)
        else:
            return make_response(target.to_dict(), 200)
    
    def patch(self, id):
        target = Part.query.filter(Part.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find part'}, 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(target, attr, data[attr])
            try: 
                db.session.add(target)
                db.session.commit()
                return make_response(target.to_dict(), 200)
            except:
                make_response({"error":"Cannot edit part"}, 400)

    def delete(self, id):
        target = Part.query.filter(Part.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find part'}, 404)
        else:
            try:
                db.session.delete(target)
                db.session.commit()
                return make_response({}, 204)
            except:
                return make_response({"error":"Cannot delete part"}, 400)
api.add_resource(GetPartbyId, '/part/<int:id>')

class GetNotes(Resource):
    def get(self):
        noteList = []
        for note in Note.query.all():
            noteList.append(note.to_dict())
        return make_response(noteList, 200)
    
    def post(self):
        new = Note(
            note = request.get_json()['note'],
            car_id = request.get_json()['car'],
            tech_id = request.get_json()['tech'],
        )
        try:
            db.session.add(new)
            db.session.commit()
            return make_response(new.to_dict(), 200)
        except:
            return make_response({'error': 'Cannot add note'}, 400)
api.add_resource(GetNotes, '/notes')

class GetNotebyId(Resource):

    def get(self, id):
        target = Note.query.filter(Note.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Note'}, 404)
        else:
            return make_response(target.to_dict(), 200)
    
    def patch(self, id):
        target = Note.query.filter(Note.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Note'}, 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(target, attr, data[attr])
            try: 
                db.session.add(target)
                db.session.commit()
                return make_response(target.to_dict(), 200)
            except:
                make_response({"error":"Cannot edit Note"}, 400)

    def delete(self, id):
        target = Note.query.filter(Note.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Note'}, 404)
        else:
            try:
                db.session.delete(target)
                db.session.commit()
                return make_response({}, 204)
            except:
                return make_response({"error":"Cannot delete Note"}, 400)
api.add_resource(GetNotebyId, '/note/<int:id>')

class GetImages(Resource):

    def get(self):
        imgList = []
        for img in Image.query.all():
            imgList.append(img.to_dict())
        return make_response(imgList, 200)
    
    def post(self):
        new = Image(
            img = request.get_json()['img'],
        )
        try:
            db.session.add(new)
            db.session.commit()
            return make_response(new.to_dict(), 200)
        except:
            return make_response({'error': 'Cannot add image'}, 400)
api.add_resource(GetImages, '/images')

class GetImagebyId(Resource):
    def get(self, id):
        target = Image.query.filter(Image.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Image'}, 404)
        else:
            return make_response(target.to_dict(), 200)
    
    def patch(self, id):
        target = Image.query.filter(Image.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Image'}, 404)
        else:
            data = request.get_json()
            for attr in data:
                setattr(target, attr, data[attr])
            try: 
                db.session.add(target)
                db.session.commit()
                return make_response(target.to_dict(), 200)
            except:
                make_response({"error":"Cannot edit Image"}, 400)

    def delete(self, id):
        target = Image.query.filter(Image.id == id).first()
        if target == None:
            return make_response({'error':'Cannot find Image'}, 404)
        else:
            try:
                db.session.delete(target)
                db.session.commit()
                return make_response({}, 204)
            except:
                return make_response({"error":"Cannot delete Image"}, 400)
api.add_resource(GetImagebyId, '/image/<int:id>')