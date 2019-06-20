#!/usr/bin/env python3

from flask import Flask, jsonify, abort, request, make_response, url_for
from jsonschema import validate

import ministac

app = Flask(__name__)

SEARCH_SCHEMA = {
  "$schema": "http://json-schema.org/draft-06/schema#",
  "title": "STAC Collection Specification",
  "description": "This object represents valid request body for the search endpoint",
  "type": "object",
  "required": [
    "collection"
  ],
  "additionalProperties": True,
  "properties": {
    "collection": {
      "title": "Collection name",
      "type": "string"
    },
    "geom": {
      "title": "Optional geojson geometry",
      "type": "object"
    },
    "startDate": {
      "title": "Start date",
      "type": "string"
    },
    "endDate": {
      "title": "End date",
      "type": "string"
    },
    "maxCloudCover": {
      "title": "Maximum allowed cloud cover",
      "type": "number"
    },
  }
}

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/ministac/api/v0/collections', methods = ['GET'])
def get_collections():
    return jsonify(ministac.collections())


@app.route('/ministac/api/v0/<string:collection>', methods = ['GET'])
def get_collection(collection):
    try:
        collection_meta = ministac.get_collection(collection)
    except Exception as e:
        abort(404)
    return jsonify(collection_meta)


@app.route('/ministac/api/v0/<string:collection>/<string:item>', methods = ['GET'])
def get_item(collection, item):
    try:
        item_meta = ministac.get_item(collection, item)
    except Exception as e:
        abort(404)
    return jsonify(item_meta)


@app.route('/ministac/api/v0/search', methods = ['POST'])
def search():
    content = request.get_json(silent=True)
    if content is None:
        abort(400)
    # Validate request json
    try:
        validate(content, SEARCH_SCHEMA)
    except Exception as e:
        abort(400)
    items = ministac.search(**content)
    return jsonify(items)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
