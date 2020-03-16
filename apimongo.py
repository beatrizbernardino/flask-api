from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
app=Flask(__name__)


app.config['MONGO_DBNAME'] = 'cars'
app.config['MONGO_URI'] = 'mongodb://mongo:27017/db_cars'

mongo = PyMongo(app)

car=mongo.db



@app.route('/carros', methods=(['GET']))
def home(): 
    for q in car.find():
        output.append({'modelo' : q['name'], 'motor' : q['motor'], 'marca' : q['marca']})
    if output:
        return jsonify({'result' : output}), 200
    else:
        return jsonify({'message' : 'No results found'}), 204
    


# @app.route('/carros/<string:motor>', methods=(['GET']))
# def carros_motor(motor): 
#     carros_motor=[carro for carro in carros if carro['motor']==motor ]
#     return jsonify(carros_motor), 200


# @app.route('/carros', methods=(['POST']))
# def novo_carro(): 
#     data=request.get_json()
#     carros.append(data)

#     return jsonify(data), 201


# @app.route('/carros/<string:modelo>', methods=(['PUT']))
# def alterar_carro(modelo):
#     for carro in carros: 
#         if carro['modelo']== modelo: 
#             carro['motor']= request.get_json().get('motor')

#             return jsonify(carros), 200
#     return jsonify({'error': 'carro não encontrado!'}), 404


# @app.route('/carros/<string:modelo>', methods=(['DELETE']))
# def deletar_carro(modelo):
#     car=[carro for carro in carros if carro[ 'modelo']==modelo]
#     carros.remove(car[0])

#     return jsonify({'carros': carros}), 200


        



if __name__ == '__main__': 
    app.run(debug=True)