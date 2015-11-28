from flask import Flask , make_response, render_template, jsonify, send_from_directory,request,redirect
import os
from werkzeug import secure_filename
import json
import random

app = Flask(__name__, instance_relative_config=True,static_url_path="/static")

@app.route('/')
def index():
	return 'Harpreet Boparai'

if __name__ == '__main__':
	app.run('0.0.0.0')
