# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:29:44 2024

@author: Chris
"""
import Character_Generator.py


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)