# coding: utf-8
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import FetchedValue
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    __tablename__ = 'user'

    Id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(255), server_default=db.FetchedValue())
    pwd = db.Column(db.String(255))
    nickname = db.Column(db.String(255))
    sex = db.Column(db.String(255))
    city = db.Column(db.String(255))
    os = db.Column(db.String(255))
    ip = db.Column(db.String(255))
    advantage = db.Column(db.String(255))
    disadvantage = db.Column(db.String(255))
    birthday = db.Column(db.String(255))
    status = db.Column(db.String(255), nullable=False, server_default=db.FetchedValue())
    five_element = db.Column(db.String(255))
    sign = db.Column(db.String(255))
    career = db.Column(db.String(255))
