#!usr/bin/env python

import flask
import json

from walmartapi.v1.api import walapi

# Loading configuration file
config_file = "config/config.json"
config = json.load(config_file)

