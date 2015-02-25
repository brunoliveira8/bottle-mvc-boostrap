# -*- coding: utf-8 -*-
from project import app
from bottle import template, request



@app.route('/', method='GET')
def index():
	from project.models.Printer import Printer
	printer = Printer()
	rows = printer.show_list()
	print rows
	return template('printer/index', rows=rows)
    



