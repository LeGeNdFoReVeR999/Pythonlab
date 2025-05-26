from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource  

app = Flask(__name__)
api = Api(app)  

recipes = []
recipe_id_counter = 1

class Recipe(Resource):
    def get(self, recipe_id):  
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                return recipe, 200
        return {"message": "Recipe not found"}, 404  

    def put(self, recipe_id):
        for recipe in recipes:
            if recipe["id"] == recipe_id:
                recipe.update(request.json)  
                return recipe, 200
        return {"message": "Recipe not found"}, 404  

class RecipeList(Resource):
    def get(self):
        return recipes, 200 
    
    def post(self):
        global recipe_id_counter
        new_recipe = request.json
        new_recipe["id"] = recipe_id_counter
        new_recipe["published"] = False
        recipes.append(new_recipe)

        response = make_response(jsonify(new_recipe), 201)
        response.headers["Location"] = f"/recipe/{recipe_id_counter}"
        recipe_id_counter += 1
        return response

class PublishRecipe(Resource):
    def put(self):
        if not recipes:
            return {"message": "No recipe to publish"}, 404
        for recipe in recipes:
            recipe["published"] = True
        return {"message": "All recipes set to published"}, 

api.add_resource(RecipeList, "/recipes")
api.add_resource(Recipe, "/recipe/<int:recipe_id>")
api.add_resource(PublishRecipe, "/recipes/publish")

if __name__ == "__main__":  
    app.run(debug=True)
