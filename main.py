from flask import Flask , make_response, render_template, jsonify, send_from_directory,request,redirect
import os
from werkzeug import secure_filename
import json
import random


@app.route('/')
def index():
	return 'Website in Progress'

