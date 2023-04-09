"""Seed file to make sample data for blogly db."""

from models import Cupcake, db
from app import app

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    Cupcake.query.delete()

    # Add cupcakes
    choco = Cupcake(flavor="Chocolate", size="large", rating=5.0)
    straw = Cupcake(flavor="Strawberry", size="large", rating=3.5)
    vanilla = Cupcake(flavor="Vanilla", size="large", rating=4.3)
    c1 = Cupcake(
        flavor="cherry",
        size="large",
        rating=5,
    )

    c2 = Cupcake(
        flavor="chocolate",
        size="small",
        rating=9,
        image="https://www.bakedbyrachel.com/wp-content/uploads/2018/01/chocolatecupcakesccfrosting1_bakedbyrachel.jpg"
    )

    # Add new objects to session, so they'll persist
    db.session.add_all([c1, c2])
    db.session.add(choco) 
    db.session.add(straw)
    db.session.add(vanilla)
    db.session.commit()

