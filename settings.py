# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
MONGO_USERNAME = 'ptr'
MONGO_PASSWORD = 'ptr'
MONGO_DBNAME = 'ptr'

RESOURCE_METHODS = ['GET','POST','DELETE']
ITEM_METHODS = ['GET','PATCH','PUT','DELETE']

DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

bodyweight = {
    'url': 'body/weight',
    'schema': {
        'weight': {
            'type': 'float',
        },
        'datetime': {
            'type': 'datetime',
        },
    }
}

bodyfat = {
    'url': 'body/fat',
    'schema': {
        'fatpct': {
            'type': 'float',
        },
        'datetime': {
            'type': 'datetime',
        },
    }
}

liftingset = {
    'url': 'lifting/set',
    'schema': {
        'exercise': {
            'type': 'string',
        },
        'datetime': {
            'type': 'datetime',
        },
        'weight': {
            'type': 'float',
        },
        'units': {
            'type': 'list',
            'allowed': ["lb","kg"],
        },
        'repetitions': {
            'type': 'int',
        },
    }
}

DOMAIN = {
    'bodyweight': bodyweight,
    'bodyfat': bodyfat,
    'liftingset': liftingset,
}
