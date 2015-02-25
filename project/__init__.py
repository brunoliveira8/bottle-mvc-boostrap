# -*- coding: utf-8 -*-
__version__ = '0.1'
from bottle import Bottle, TEMPLATE_PATH
import sqlite3
app = Bottle()
TEMPLATE_PATH.append("./project/views/")
TEMPLATE_PATH.remove("./views/")
from project.controllers import *
