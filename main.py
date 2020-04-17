#!usr/bin/env python

from flask import Flask, request, jsonify
import json

from walmartapi.v1.api import Walapi

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
    return "Success"

if __name__ == "__main__":
    app.run()
