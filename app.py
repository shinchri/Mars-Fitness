from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, User
import os
import stripe

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
    "price_id": os.environ["STRIPE_PRICE_ID"]
}

stripe.api_key = stripe_keys["secret_key"]

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)

    @app.route('/')
    def home():
        return render_template('pages/home.html')

    return app

app = create_app()

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()