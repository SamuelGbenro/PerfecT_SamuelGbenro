from flask_restful import Resource
from models.industry import IndustryModel


class Industry(Resource):
    def get(self, name):
        industry = IndustryModel.find_by_name(name)
        if industry:
            return industry.json()
        return {'message': 'Industry not found'}, 404

    def post(self, name):
        if IndustryModel.find_by_name(name):
            return {'message': "An industry with name '{}' already exists.".format(name)}, 400

        industry = IndustryModel(name)
        try:
            industry.save_to_db()
        except:
            return {'message': 'An error occured while adding industry.'}, 500

        return industry.json(), 201

    def delete(self, name):
        industry = IndustryModel.find_by_name(name)
        if industry:
            industry.delete_from_db()
        return {'message': 'Industry deleted'}

class IndustryList(Resource):
    def get(self):

        return {'industry': [industry.json() for industry in IndustryModel.query.all()]}