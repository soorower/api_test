from flask import request
import flask
import requests
from bs4 import BeautifulSoup as bs
app = flask.Flask(__name__)

@app.route('/',methods = ['GET'])

def home():
  arg = request.args['arg']
  r = requests.get(arg)
  soup = bs(r.content,'html.parser')
  # Product_name = str(soup)[10:29]
  
  return soup