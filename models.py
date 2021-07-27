from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine, Sequence
from flask_sqlalchemy import SQLAlchemy
import json
import os
import datetime

from sqlalchemy.sql.functions import user

db = SQLAlchemy()

def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    db.create_all()
    return db

class User(db.Model):

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(db.String(200), nullable=False)
    created_on = Column(DateTime, default=datetime.datetime.now(), nullable=False)

    def __init__(self, first_name, last_name, email, password, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.created_on = created_on
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class StripeCustomer(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    stripeCustomerId = Column(String(255), nullable=False)
    stripeSubscriptionId = Column(String(255), nullable=False)

    def __init__(self, user_id, stripeCustomerId, stripeSubscriptionId):
        self.user_id = user_id
        self.stripeCustomerId = stripeCustomerId
        self.stripeSubscriptionId = stripeSubscriptionId

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
