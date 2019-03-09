from flask import Flask, request
from flask_restful import Resource, Api, regparse
from flask_jwt import JWT, jwt_required
from config import SECRET_KEY, authenticate, identity

app = Flask(__name__)
app.secret_key = SECRET_KEY
api = Api(app)
# JWT
jwt = JWT(app, authenticate, identity)

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': 'None'}, 404

    def post(self, name):
        data = request.get_json()
        newItem = {
            'name': name,
            'price': data['price']
        }
        items.append(newItem)
        return newItem, 201  # Created code

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message": "deleted seccessfully"}

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item: {
                'name': name,
                'price': data['price']
            }
            items.append(item)
        else:
            item.update(data['price'])
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
app.run(port=5000, debug=True)
