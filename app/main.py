import bottle
import os
import random


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

@bottle.get('/')
def index():
    return {
        "Hello World": ""
    }

@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#0000FF',
        'taunt': 'I can\'t even',
        'head_url': head_url,
        'name': 'Basic AI'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': random.choice(directions),
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
    
    #comment
