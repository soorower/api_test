from flask_restful import Resource

todos = [
  {
    "id": 1,
    "item": "Create sample app",
    "status": "Completed sorower"
  },
  {
    "id": 2,
    "item": "Deploy in Heroku",
    "status": "Open soorwer"
  },
  {
    "id": 3,
    "item": "Publish",
    "status": "Oppppppppppppppen"
  }
]

class Todo(Resource):
  def get(self, id):
    for todo in todos:
      if(id == todo["id"]):
        return todo, 200
    return "Item not found for the id: {}".format(id), 404

#   def put(self, id):
#     for todo in todos:
#       if(id == todo["id"]):
#         todo["item"] = request.form["data"]
#         todo["status"] = "Open"
#         return todo, 200
#     return "Item not found for the id: {}".format(id), 404