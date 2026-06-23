from flask import Flask, request, jsonify, url_for, Blueprint, current_app
from flask_cors import CORS
from sqlalchemy import select, func
from api.models import db, User

api = Blueprint('api', __name__)

CORS(api)


@api.route('/temperature', methods=['GET'])
def get_temperature():
    result = User.query.all()
    return jsonify([u.serialize() for u in result]), 200



