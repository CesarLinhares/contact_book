connection_links = {
    'joao': {
        'mongo_link': "postgres://root:example@localhost:1231",
        'redis_link': 'redis://localhost:1230'
    },
    'cesar': {
        'mongo_link': 'postgres://localhost:27017',
        'redis_link': 'redis://localhost:6379'
    }
}

user = connection_links.get('joao')
