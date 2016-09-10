#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
please read it
http://a2c.bitbucket.org/flask/quickstart.html
'''
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/output/<int:post_id>')
def menu_output():
   # show the menu
   pass

@app.route('/input/')
def menu_input():
   return "you should enter something here"
   pass

if __name__ == '__main__':
    app.run(debug=True)

