#!/usr/bin/env python3

from flask import Flask, jsonify, abort, request, make_response, url_for

import ministac

app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
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


if __name__ == '__main__':
    app.run(debug=True)
