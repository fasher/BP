#!/bin/python

import os
import random
from flask import Flask, send_from_directory

static_folder = os.path.join(os.pardir,'resources')
app = Flask(__name__)
resources_dir = os.path.join(app.root_path,'resources')

@app.route('/',defaults={'path': '' })
@app.route('/<path:path>')
def display_random_img(path):
  files = os.listdir(resources_dir)
  return send_from_directory(resources_dir,random.choice(files))
