connection_links = {
    'joao': {
        'mongo_link': "mongodb://root:example@localhost:1231",
        'redis_link': 'redis://localhost:6379'
    },
    'cesar': {
        'mongo_link': 'mongodb://localhost:27017',
        'redis_link': 'redis://localhost:6379'
    }
}

user = connection_links.get('joao')
