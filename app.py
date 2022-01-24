from flask import request
import flask
import requests
from bs4 import BeautifulSoup as bs
app = flask.Flask(__name__)

@app.route('/',methods = ['GET'])

def home():
  headers = {

  'authority':'api.takealot.com',
  'method':'GET',
  'path':'/rest/v-1-10-0/product-details/PLID72874143?platform=desktop',
  'scheme':'https',
  'accept':'*/*',
  'accept-encoding':'gzip, deflate, br',
  'accept-language':'en-US,en;q=0.9',
  'cache-control':'no-cache',
  'origin':'https',
  'pragma':'no-cache',
  'referer':'https',
  'sec-ch-ua':'" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
  'sec-ch-ua-mobile':'?0',
  'sec-ch-ua-platform':'"Windows"',
  'sec-fetch-dest':'empty',
  'sec-fetch-mode':'cors',
  'sec-fetch-site':'same-site',
  'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
  }
  arg = request.args['arg']
  r = requests.get(arg,headers=headers)
  soup = bs(r.content,'html.parser')
  # Product_name = str(soup)[10:29]
  sou = str(soup)
  return sou