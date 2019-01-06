************
Ministac-api
************

*JSON REST API for `ministac <http://github.com/loicdtx/ministac>`_*

List of functionalities
=======================

Method  endpoint   description
GET   api/v0/collections  get a list of available collections
GET   api/v0/<collection-name>  get the metadata of a given collections
GET   api/v0/<collection-name>/<item-id>   get the metadata of a given item
GET   api/v0/search   search a list of items using various filters (spatial, temporal, cloud cover)	


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

    r = requests.get('http://127.0.0.1:5000/ministac/api/v0/search', json=params)
    pprint(r.json())
