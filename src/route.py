from http import HTTPStatus
from flask import Flask, request, jsonify

from src.snack import Snack, Ingredient

JSON_HEADER = {'Content-Type': 'application/json'}

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/api/lanche/', methods=['GET'])
def get_snacks():
    return jsonify(Snack.get_all_snacks_names()), HTTPStatus.OK, JSON_HEADER


@app.route('/api/ingrediente/de/<id_lanche>', methods=['GET'])
def get_snack_ingredients_and_price(id_lanche):
    try:
        id_lanche = int(id_lanche)
    except ValueError:
        return bad_request('<id_lanche> should be an integer')

    if id_lanche < 0 or id_lanche > 3:
        return bad_request('<id_lanche> should be {0, 1, 2, 3}')

    return jsonify(Snack.get_snack_ingredients_and_price_by_id(id_lanche)), HTTPStatus.OK, JSON_HEADER


@app.route('/api/ingrediente/', methods=['GET'])
def get_ingredients():
    return jsonify(Ingredient.get_all_ingredients_names()), HTTPStatus.OK, JSON_HEADER


def bad_request(message):
    return jsonify({'error': message}), HTTPStatus.BAD_REQUEST, JSON_HEADER
