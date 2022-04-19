connection_links = {
    'joao': {
        'mongo_link': "mongo://root:example@localhost:1231",
        'redis_link': 'redis://localhost:1230'
    },
    'cesar': {
        'mongo_link': 'mongo://localhost:27017',
        'redis_link': 'redis://localhost:6379'
    }
}

user = connection_links.get('joao')
