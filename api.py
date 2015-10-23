#!/usr/bin/python

import json
from bottle import route, run, request, abort
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

connection = MongoClient('localhost', 27017)
db = connection.ptr


def response(dictionary):
    return dumps(dictionary)


def load_data():
    """
    Return a dictionary loaded from parsed json data.
    """
    data = request.body.readline()
    if not data:
        abort(400, 'no data received')
    entity = json.loads(data)
    return entity


@route('/tasks')
def tasks_list():
    return response([o for o in db['tasks'].find()])


@route('/tasks/<id>', method='GET')
def tasks_get(id):
    return response(db['tasks'].find_one({'_id': ObjectId(id)}))


@route('/tasks', method='POST')
def tasks_post():
    entity = load_data()
    result = db['tasks'].insert_one(entity)
    return response(db['tasks'].find_one({'_id': result.inserted_id}))


@route('/tasks/<id>', method='PUT')
def tasks_update(id):
    entity = load_data()
    result = db['tasks'].find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': entity})
    return response(db['tasks'].find_one({'_id': ObjectId(id)}))

if __name__ == '__main__':
    run(host='0.0.0.0', port=8001)
