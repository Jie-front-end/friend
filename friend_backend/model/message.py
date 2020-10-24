# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Message(db.Model):
    __tablename__ = 'message'

    Id = db.Column(db.Integer, primary_key=True)
    send = db.Column(db.String(255))
    accept = db.Column(db.String(255))
    time = db.Column(db.String(255))
    content = db.Column(db.String(2550))
    status = db.Column(db.Integer, server_default=db.FetchedValue())
