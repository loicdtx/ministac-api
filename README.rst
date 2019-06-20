************
Ministac-api
************

*JSON REST API for `ministac <http://github.com/loicdtx/ministac>`_ *

Resources
=========

List of resources
-----------------



+-------------+------------------------------------------+-----------------------------------------------------------------------+
| HTTP method | URI                                      | Action                                                                |
+=============+==========================================+=======================================================================+
| GET         | /ministac/v0/collections                 | Get a list of available collections                                   |
+-------------+------------------------------------------+-----------------------------------------------------------------------+
| GET         | /ministac/v0/<collection-name>           | Get the metadata of a given collection                                |
+-------------+------------------------------------------+-----------------------------------------------------------------------+
| GET         | /ministac/v0/<collection-name>/<item-id> | Get the metadata of a given item                                      |
+-------------+------------------------------------------+-----------------------------------------------------------------------+
| POST        | /ministac/v0/search                      | Search a list of items using filters (spatial, temporal, cloud cover) |
+-------------+------------------------------------------+-----------------------------------------------------------------------+



Example usage with python
=========================

.. code-block:: python

    import requests
    import datetime as dt
    from pprint import pprint

    # Get all available collections
    r = requests.get('http://127.0.0.1:5000/ministac/api/v0/collections')
    pprint(r.json())


    # Get metadata of a collection
    r = requests.get('http://127.0.0.1:5000/ministac/api/v0/landsat_sr_8')
    pprint(r.json())


    # Get metadata of an item
    r = requests.get('http://127.0.0.1:5000/ministac/api/v0/landsat_sr_8/LC08_L1TP_028045_20171121_20171206_01_T1')
    pprint(r.json())


    # Search items using various filters
    params = {'collection': 'landsat_sr_8',
              'maxCloudCover': 12,
              'endDate': dt.datetime(2017, 12, 1).isoformat()}

    r = requests.post('http://127.0.0.1:5000/ministac/api/v0/search', json=params)
    pprint(r.json())


HTTP status codes
=================

``200``: OK

``400``: Bad request

``404``: Not found


Install
=======

You must first configure `ministac <https://github.com/loicdtx/ministac>`_ (database setup and configuration file), then.


Locally
-------


.. code-block:: bash

    git clone git@github.com:loicdtx/ministac-api.git
    cd ministac-api
    pip install -r requirements.txt
    pip install -e .
    export FLASK_APP=api
    flask run


Using docker
------------

.. code-block:: bash

    git clone https://github.com/loicdtx/ministac-api.git
    cd ministac-api.git
    docker build -t ministac-api:latest .
    docker run --name ministac-api --rm -d -p 5000:5000 -v ~/.ministac:/root/.ministac ministac-api