# -*- coding: utf-8 -*-
import sqlite3


class Printer(object):

    def show_list(self):
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
        result = c.fetchall()
        c.close()
        return result

