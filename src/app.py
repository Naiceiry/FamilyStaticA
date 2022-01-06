"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Get para retornar todos los miembros
@app.route('/members', methods=['GET'])
def get_family_members():
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200

#get para retornar un miembro
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id): #recibe el id
    member = jackson_family.get_member(id) #compara y responde 200 o 400
    
    if member is not None:
        return jsonify(member), 200
    else:
        return "Member Not FOUND", 400

# post para sumar miembro
@app.route('/member', methods=['POST'])
def add_member():
    member = request.json 
    if not member:
        return jsonify({"msj":"invallid imput"}), 400
    jackson_family.add_member(member)
    return jsonify({"msj":"Member added"}), 200

#Eliminar un miembro
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = jackson_family.delete_member(member_id)
    if not member:
        return jsonify({"Msj":"El id no existe!!"})
    print("Miembro eliminado!!")
    return jsonify(member)

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)

