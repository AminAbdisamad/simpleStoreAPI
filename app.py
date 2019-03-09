from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {'name': 'Gaandi',
     "items": {
         "id": 1,
         "name": "Shoes",
         "price": 14.0,
     }

     },
    {'name': 'Garow',
     "items": {
         "id": 2,
         "name": "Watches",
         "price": 11.99,
     }

     }
]
# Home
@app.route('/')
def home():
    return render_template('index.html')
# Create Store
@app.route('/store', methods=['POST'])
def createStore():
    requestData = request.get_json()
    newStore = {
        "name": requestData["name"],
        "items": []
    }
    stores.append(newStore)
    return jsonify(newStore)

# Get all stores
@app.route('/store')
def getStore():
    return jsonify({"store": stores})

# Get specific store
@app.route('/store/<string:name>')
def getItem(name):
    # return store with specic name
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({"message": "Store not found"})


# FInd item in the store
@app.route('/store/<string:name>/item')
def getItems(name):
    # return store with specic name
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({"message": "item not found"})


@app.route('/store/<string:name>/item', methods=['POST'])
def createItemInStore(name):
    rData = request.get_json()
    for store in stores:
        if store['name'] == name:
            newItem = {
                'id': rData['id'],
                'name': rData['name'],
                'price': rData['price']
            }
            store['items'].append(newItem)
            return jsonify(newItem)
    return jsonify({"message": "store not found "})


# Start app
app.run(port=4000)
