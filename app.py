from flask import request
import flask
import requests
import json
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

  check = request.args['token']
  link1 = request.args['link']
#   link2 = link1.split('/')[-1]
#   link = f'https://api.takealot.com/rest/v-1-10-0/product-details/{link2}?platform=desktop'
#   if check=='Jx8SeUYilsP0h2000':
#     r = requests.get(link,headers=headers)
#     soup = bs(r.content,'html.parser')


#     if '"title":' in str(soup)[:50]:

#       data = json.loads(str(soup))
#       product_name= data.get('title')
#       price = data.get('buybox').get('prices')[0]
#       stock = data.get('stock_availability').get('status')

#       images = []
#       if type(data.get('gallery').get('images'))==list:
#           for i in data.get('gallery').get('images'):
#               images.append(i.replace('{size}','zoom'))
#       else:
#           images = data.get('gallery').get('images')
#       data_set = {
#           'Product Name': product_name,
#           'Price': price,
#           'Stock Availability': stock,
#           'Images': images
#       }

#       jsons = json.dumps(data_set)
#     else:
#         data_set = {
#             'Error': 'Something Went Wrong, try after some seconds'
#         }
#         jsons = json.dumps(data_set)
#   else:
#       data_set = {
#             'TOKEN ERROR': 'INVALID TOKEN'
#         }
#       jsons = json.dumps(data_set)
  return 'hello'