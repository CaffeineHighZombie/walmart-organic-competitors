import flask
from flask import request, jsonify

from walapi import walapi

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/lookup', methods=['GET'])
def product_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'productId' in request.args:
        id = int(request.args['productId'])
    else:
        return "Error: No id field provided. Please specify an id."

    try:
        data = walapi.product_lookup(id)
        product_title = data["name"]
        titles = product_title.split()
        ranking = walapi.build_ranking(titles)
        final = walapi.consolidate_ranking(ranking)
        response = {}
        response["productId"] = id
        response["competitors"] = final
        return jsonify(response)
    except Exception as e:
        return e

app.run()