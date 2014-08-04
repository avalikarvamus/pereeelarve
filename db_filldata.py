#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#    Copyright 2014 Madis Veskimeister <madis@pingviinitiivul.ee>
#

from app.config import SQLALCHEMY_DATABASE_URI
from app import db
import os.path
from app.models import User, Budget, BudgetLine
from flask.ext.security.utils import encrypt_password

def fillData():
    toomas = User(name="Vana", firstname="Toomas", email="toomas@utoopia.eu", password=encrypt_password("123test"))
    db.session.add(toomas)
    db.session.commit()

fillData()
