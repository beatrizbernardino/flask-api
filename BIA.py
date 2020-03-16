from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
import socket
import pprint




app=Flask(__name__)




mongo = MongoClient( 'mongodb+srv://beatriz:pbia02@cluster0-sbwnl.mongodb.net/Processo_seletivo?retryWrites=true&w=majority')

db = mongo['carros2020']
collection = db['cars']



# carros= [
#     { 
#         'modelo': 'HB20',
#         'motor': '1.6',
#         'marca': 'Hyundai'
#     },

#     { 
#         'modelo': 'XC60',
#         'motor': '2.0',
#         'marca': 'Volvo'
#     },

#     { 
#         'modelo': 'Compass',
#         'motor': '2.0',
#         'marca': 'Jeep'
#     },

#     { 
#         'modelo': 'Fox',
#         'motor': '1.6',
#         'marca': 'Volkswagen'
#     },

#     { 
#         'modelo': 'Evoque',
#         'motor': '2.0',
#         'marca': 'Land Rover'
#     },

#     { 
#         'modelo': 'Polo',
#         'motor': '1.6',
#         'marca': 'Volkswagen'
#     }


# ] 




@app.route('/carros', methods=(['GET']))
def carros_total():
	car = collection
	goals = []
	goal = car.find()
	for j in goal:
		j.pop('_id')
		goals.append(j)
	return jsonify(goals), 200	





@app.route('/carros/<string:motor>', methods=(['GET']))
def carros_motor(motor): 
	car = collection
	goals = []
	goal = car.find({"motor": motor})
	for j in goal:
		j.pop('_id')
		goals.append(j)
	return jsonify(goals), 200	


@app.route('/novocarro', methods=(['POST']))
def novo_carro(): 

   data = request.get_json()
   if data:
        modelo = request.json['modelo']
        motor = request.json['motor']
        marca = request.json['marca']
        existing_car = collection.find_one({'modelo' : modelo})
        if existing_car is None:
            collection.insert({'modelo' : modelo, 'motor' : motor, 'marca' : marca})
            return jsonify({'message' : 'Modelo <' + modelo  + '> created successfully'}), 201
        else:
            return jsonify({'message' : 'Modelo '< + modelo + '> already exists'}), 409
   else: 
        return jsonify({'message' : 'No data provided'}), 400  



@app.route('/carros/<string:modelo>', methods=(['PUT']))
def alterar_carro(modelo):
    data = request.get_json()
    if data:
        motor = request.json['motor']
        existing_room = collection.find_one({'modelo' : modelo})
        if existing_room:
            collection.update_one({"modelo": modelo},
                            {"$set": {'motor' : motor}})

            return jsonify({'message' : 'Motor <' + motor  + '> updated successfully'}), 200
        else:
            return jsonify({'message' : 'Motor <' + motor + '> does not exist'}), 409
    else: 
        return jsonify({'message' : 'No data provided'}), 400


@app.route('/carros/<string:modelo>', methods=(['DELETE']))
def deletar_carro(modelo):
    if modelo:
        existing_car = collection.find_one({'modelo' : modelo})
        if existing_car:
            collection.delete_one({"modelo": modelo})
            return jsonify({'message' : 'Modelo <' + modelo  + '> deleted successfully'}), 200
        else:
            return jsonify({'message' : 'Modelo <' + modelo + '> does not exist'}), 404
    else:
        return jsonify({'message' : 'No data provided'}), 400



        



if __name__ == '__main__': 
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
