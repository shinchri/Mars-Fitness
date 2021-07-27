from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort, jsonify
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

    @app.route("/config")
    def get_publishable_key():
        stripe_config = {"publicKey": stripe_keys["publishable_key"]}
        return jsonify(stripe_config)

    @app.route("/create-checkout-session")
    def create_checkout_session():
        domain_url = "http://localhost:5000/"
        stripe.api_key = stripe_keys["secret_key"]

        try:
            checkout_session = stripe.checkout.Session.create(
                # You should get the user id here and pass it along as 'client_reference_id'
                #
                # this will alow you to associate the Stripe session with
                # the user saved in your database
                # 
                # example: client_reference_id=user.id,
                success_url = domain_url + "success?session_id={CHECKOUT_SESSION_ID}",
                cancel_url = domain_url + "cancel",
                payment_method_types=["card"],
                mode="subscription",
                line_items=[{
                    "price": stripe_keys["price_id"],
                    "quantity": 1,
                }]
            )
            return jsonify({"sessionId": checkout_session["id"]})
        except Exception as e:
            return jsonify(error=str(e)), 403

    return app

app = create_app()

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()