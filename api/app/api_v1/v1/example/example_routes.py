# -*- coding: utf-8 -*-
#########################################################
# All rights by SoftPymes
# Routes Example
#########################################################

from flask import request, jsonify
from app.api_v1 import api
from app.controllers import ExampleController as Controller

from datetime import datetime
dt = datetime.now()

@api.route('/api/v1/index', methods=['GET'])
def get_index():
    response = Controller.get_index()
    return jsonify(data=response)

@api.route('/api/v1/', methods=['GET'])
def get_index_many():
    response = Controller.get_index_many()
    return jsonify(data=response)

@api.route('/api/v1/<id>', methods=['GET'])
def get_index_one():
    response = Controller.get_index_one()
    return jsonify(data=response)

@api.route('/api_v1/v1', methods=['POST'])
def post_index():
    data = request.get_json(force=True)
    if Controller.post_index(data):
        response = Controller.post_index(data)
        return jsonify({
            "code": 200,
            "data": response,
            "status": "ok",
            "message": "Usuario agregado exitosamente",
            "time": dt
        })
    return jsonify({
        "code": 500,
        "data": {},
        "status": "error",
        "message": "Error agregando usuario",
        "time": dt
        })

@api.route('/api/v1/<id>', methods=['PUT'])
def put_index():
    data = request.get_json(force=True)
    id_arg = request.args.get('id')

    if Controller.put_index(id_arg, data):
        response = Controller.put_index(id_arg, data)
        return jsonify({
                "code": 200,
                "data": response,
                "status": "ok",
                "message": "Usuario editado exitosamente",
                "time": dt
                })
    return jsonify({
        "code": 500,
        "data": {},
        "status": "error",
        "message": "Error editando usuario",
        "time": dt
        })

@api.route('/api/v1/<id>', methods=['DELETE'])
def delete_index():
    id_arg = request.args.get('id')
    if Controller.delete_index(id_arg):
        response = Controller.delete_index(id_arg)
        return jsonify({
            "code": 200,
            "data": response,
            "status": "ok",
            "message": "Usuario eliminado exitosamente",
            "time": dt
            })
    return jsonify({
        "code": 500,
        "data": {},
        "status": "error",
        "message": "Error eliminando usuario",
        "time": dt
        })