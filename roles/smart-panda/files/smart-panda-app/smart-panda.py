#!/bin/python

from flask import Flask

app = Flask(__name__)

global counter
counter = 0

@app.route('/',defaults={'path': '' }, methods=['POST'])
@app.route('/<path:path>',methods=['POST'])
def count_posts(path):
  global counter
  counter += 1
  return 'OK counted'


@app.route('/',defaults={'path': '' }, methods=['GET'])
@app.route('/<path:path>',methods=['GET'])
def show_count(path):
  global counter
  return  str(counter) + ' counted'
