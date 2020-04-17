from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/heroes')
def heroes_collection():
    return jsonify(HEROES)


@app.route('/api/heroes/<int:hero_id>')
def heroes_item(hero_id):
    for hero in HEROES:
        if hero_id == hero['id']:
            return jsonify(hero)
    else:
        return "Error", 404


HEROES = [
    {'id': 1, 'name': 'Mr. Nice', 'Birth': datetime(2000, 10, 19)},
    {'id': 2, 'name': 'Bombasto', 'Birth': datetime(1996, 11, 3)},
    {'id': 3, 'name': 'Magneta', 'Birth': datetime(1980, 12, 9)},
    {'id': 4, 'name': 'RubberMan', 'Birth': datetime(1985, 9, 17)},
    {'id': 5, 'name': 'Dr IQ', 'Birth': datetime(1998, 3, 18)},
];
