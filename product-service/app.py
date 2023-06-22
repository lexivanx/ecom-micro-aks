from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Replace with Azure SQL Database URI
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    inventory = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Product %r>' % self.name

@app.route('/products', methods=['GET'])
def get_products():
    try:
        products = Product.query.all()
        return jsonify([str(product) for product in products])
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product:
            return jsonify(str(product))
        else:
            return jsonify({'message': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('inventory'):
        return jsonify({'message': 'Bad Request'}), 400
    try:
        new_product = Product(name=data['name'], inventory=data['inventory'])
        db.session.add(new_product)
        db.session.commit()
        return jsonify({'message': 'New product added'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

if __name__ == '__main__':
    db.create_all()  # Creates database tables
    app.run(debug=True, host='0.0.0.0')
