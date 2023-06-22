from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Replace with Azure SQL Database URI
db = SQLAlchemy(app)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1)

    def __repr__(self):
        return '<Order %r>' % self.id

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([str(order) for order in orders])

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    
    # Check if the user exists
    user_response = requests.get(f'http://user-service:5000/users/{data["user_id"]}')
    if user_response.status_code != 200:
        return jsonify({'message': 'User not found'}), 404

    # Check if the product exists and has enough inventory
    product_response = requests.get(f'http://product-service:5000/products/{data["product_id"]}')
    if product_response.status_code != 200:
        return jsonify({'message': 'Product not found'}), 404
    
    product_data = product_response.json()
    if product_data['inventory'] < data['quantity']:
        return jsonify({'message': 'Not enough product in inventory'}), 400

    # Create the order
    new_order = Order(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'New order placed'}), 201

if __name__ == '__main__':
    db.create_all()  # Creates database tables
    app.run(debug=True, host='0.0.0.0')
