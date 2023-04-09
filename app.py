"""Blogly application."""


from flask import Flask, request, redirect, render_template, jsonify
from models import Cupcake, db, connect_db
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)

with app.app_context():

    connect_db(app)
    db.create_all()

@app.route("/")
def show_cupcakes():
    """Show all cupcakes"""
    return render_template('index.html')

@app.route("/api/cupcakes")
def get_all_cupcakes():
    """Return JSON of all cupcakes"""
    
    cupcakes = Cupcake.query.all()
    cupcakes = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=cupcakes)

@app.route("/api/cupcakes/<int:id>")
def get_cupcake(id):
    """Return JSON of a cupcake given an id"""
    
    cupcake = Cupcake.query.get_or_404(id)
    cupcake = cupcake.serialize()

    return jsonify(cupcakes=cupcake)

@app.route("/api/cupcakes", methods=['POST'])
def add_cupcake():
    """
        Create new cupcake from posted data and add to DB
        returns JSON of added cupcake and 201 message
    """

    flavor = request.json['flavor']
    size = request.json['size']
    rating = request.json['rating']
    image = request.json['image']

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    
    new_cupcake = jsonify(cupcakes=new_cupcake.serialize())

    return (new_cupcake, 201)


@app.route("/api/cupcakes/<int:id>", methods=['PATCH'])
def update_cupcake(id):
    """
        Update a cupcake given an id
        Return JSON of updated cupcake
    """
    
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json['flavor']
    cupcake.size = request.json['size']
    cupcake.rating = request.json['rating']
    cupcake.image = request.json['image']

    db.session.add(cupcake)
    db.session.commit()

    cupcake = cupcake.serialize()

    return jsonify(cupcakes=cupcake)

@app.route("/api/cupcakes/<int:id>", methods=['DELETE'])
def delete_cupcake(id):
    """
        Delete a cupcake given an id
        Return JSON with success message
    """
    
    cupcake = Cupcake.query.get_or_404(id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({'message' : 'Deleted'})

