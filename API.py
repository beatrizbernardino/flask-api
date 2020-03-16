from flask import Flask, jsonify, request


app=Flask(__name__)

carros= [
    { 
        'modelo': 'HB20',
        'motor': '1.6',
        'marca': 'Hyundai'
    },

    { 
        'modelo': 'XC60',
        'motor': '2.0',
        'marca': 'Volvo'
    },

    { 
        'modelo': 'Compass',
        'motor': '2.0',
        'marca': 'Jeep'
    },

    { 
        'modelo': 'Fox',
        'motor': '1.6',
        'marca': 'Volkswagen'
    },

    { 
        'modelo': 'Evoque',
        'motor': '2.0',
        'marca': 'Land Rover'
    },

    { 
        'modelo': 'Polo',
        'motor': '1.6',
        'marca': 'Volkswagen'
    }


]



# INSIRA SEU CÓDIGO
        



if __name__ == '__main__': 
    app.run(debug=True)