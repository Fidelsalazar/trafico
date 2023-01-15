from flask import  Blueprint, jsonify

#Modelos
from models.BusModel import BusModel

main = Blueprint('bus_print', __name__)

@main.route('/')
def get_bus():
  try:
    buss = BusModel().get_bus()
    return jsonify(buss)
  except Exception as ex:
      return jsonify({'message':str(ex)}),500

@main.route('/rtime')   
def get_bus_rtime():
  try:
    buss = BusModel().get_bus_rtime()
    if buss != None:
      return jsonify(buss)
    else:
      return jsonify({}), 404

  except Exception as ex:
      return jsonify({'message':str(ex)}),500