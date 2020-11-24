#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'
from exts import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    isdelete = db.Column(db.Boolean, default=False)
    rdatetime = db.Column(db.DateTime, default=datetime.now())

    def __str__(self):
        return self.username