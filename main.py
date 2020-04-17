#!usr/bin/env python

from flask import Flask, request, jsonify
import json

from walmartapi.v1.api import Queryapi

# Loading configuration file
config_file = "config/config.json"
with open(config_file) as filehand:
    config = json.load(filehand)

app = Flask(__name__)
# Checking for debug value and proceed accordingly
if config["debug"]:
    app.config["DEBUG"] = True

@app.route('/api/v1/lookup', methods=['GET'])
def product_id():
    # Check if an productId was provided as part of the URL.
    # If productId is provided, assign it to a variable.
    # If no productId is provided, display an error in the browser.
    if 'productId' in request.args:
        product_id = int(request.args['productId'])
    else:
        return "Error: No id field provided. Please specify an productId."
    
    api_key = config["walmart_api_key"]
    product_query = Queryapi(api_key)
    final_ranking = product_query.get_ranking(product_id)
    response = {}
    response["productId"] = product_id
    response["competitors"] = final_ranking
    return jsonify(response)


if __name__ == "__main__":
    app.run()
