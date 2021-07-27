from flask import Flask, render_template, request, Response, flash, redirect, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, User
import os
import stripe

stripe_keys = {
    "secret_key": os.environ["STRIPE_SECRET_KEY"],
    "publishable_key": os.environ["STRIPE_PUBLISHABLE_KEY"],
    "price_id": os.environ["STRIPE_PRICE_ID"],
    "endpoint_secret": os.environ["STRIPE_ENDPOINT_SECRET"]
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

    @app.route("/success")
    def success():
        return render_template("pages/success.html")
    
    @app.route("/cancel")
    def cancel():
        return render_template("pages/cancel.html")

    @app.route("/webhook", methods=["POST"])
    def stripe_webhook():
        payload = request.get_data(as_text=True)
        sig_header = request.headers.get("Stripe_Signature")

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, stripe_keys["endpoint_secret"]
            )
        except ValueError as e:
            #Invalid payload
            return "Invalid payload", 400
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            return "Invalid signature", 400
        
        # Handle the checkout.session.completed event
        if event["type"] == "checkout.session.completed":
            session = event["data"]["object"]

            # Fullsill the purchase
            handle_checkout_session(session)
        
        return "Success", 200
    
    def handle_checkout_session(session):
        # Here you should fetch the details from the session and save the relevant information
        # to the database (e.g. associate the user with thier subscription)
        print("Subscription was successful.")

    return app

app = create_app()

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

if __name__ == '__main__':
    app.run()