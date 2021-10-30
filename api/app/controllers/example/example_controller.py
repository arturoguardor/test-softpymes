# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Controller Example
#########################################################

from app.exception import InternalServerError
from app.models import ExampleModel
from app import db


class ExampleController:

    @staticmethod
    def get_index():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)


    @staticmethod
    def get_index_many():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def get_index_one():
        try:
            response = {
                'ok': True,
                'message': 'Response OK, method get_index'
            }
            return response
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def post_index(data):
        try:
            name = data['name']
            identification = data['description']
            description = data['identification']
            status = data['status']

            if ExampleModel.validate_name_permit(name, identification):
                ExampleModel.save(name)
                ExampleModel.save(identification)
                ExampleModel.save(description)
                ExampleModel.save(status)

                return ExampleModel.export_data([name,identification,description,status])
            return False
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)

    @staticmethod
    def put_index(id,data):
        try:
            name = data['name'],
            identification = data['description'],
            description = data['identification'],
            status = data['status']

            update_data = ExampleModel.query.get(id)
            update_name = update_data['name']
            update_description = update_data['description']
            update_identification = update_data['identification']
            update_status = update_data['status']

            if ExampleModel.validate_name_permit(update_name, update_identification):
                ExampleModel.name = update_name
                ExampleModel.identification = update_identification
                ExampleModel.description = update_description
                ExampleModel.status = update_status

                return ExampleModel.export_data([id,name,identification,description,status])
            return False
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)


    @staticmethod
    def delete_index(id):
        try:
            delete_data = ExampleModel.query.get(id)
            ExampleModel.delete(delete_data)
            return True
        except Exception as e:
            print('Error: {er}'.format(er=e))
            raise InternalServerError(e)