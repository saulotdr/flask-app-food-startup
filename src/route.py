import logging
from http import HTTPStatus

from fastjsonschema import JsonSchemaException
from flask import Flask, request, jsonify

from src import constants
from src.order import Order
from src.sale import Sale
from src.snack import Snack, Ingredient
from src.validation import validate_payload


""" Logger """
logger = logging.getLogger(__name__)

""" Flask configuration """
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = constants.PRETTY_PRINT


@app.route('/api/lanche/', methods=['GET'])
def get_snacks():
    logger.debug("get_snacks()")
    return ok(Snack.get_all_snacks_names())


@app.route('/api/lanche/<id_lanche>', methods=['GET'])
@app.route('/api/ingrediente/de/<id_lanche>', methods=['GET'])
def get_snack_ingredients_and_price(id_lanche):
    logger.debug("Received request. id_lanche {0}".format(id_lanche))
    try:
        id_lanche = int(id_lanche)
    except ValueError:
        return bad_request(constants.MESSAGE_SHOULD_BE_INTEGER_PTBR, input_received=id_lanche)

    if id_lanche < 0 or id_lanche > 3:
        return bad_request(constants.MESSAGE_SHOULD_HAVE_A_VALID_SNACKID_PTBR, input_received=id_lanche)

    return ok(Snack.get_snack_info_per_id(id_lanche))


@app.route('/api/ingrediente/', methods=['GET'])
def get_ingredients():
    logger.debug("Received request")
    return ok(Ingredient.get_all_ingredients_names())


@app.route('/api/promocao/', methods=['GET'])
def get_sales():
    logger.debug("Received request")
    return ok(Sale.get_all_sales())


@app.route('/api/pedido/<id_lanche>', methods=['PUT'])
def put_snack_in_shopping_cart(id_lanche):
    logger.debug("Received request. id_lanche {0}".format(id_lanche))

    # id_lanche is an integer?
    try:
        id_lanche = int(id_lanche)
    except ValueError:
        return bad_request(constants.MESSAGE_SHOULD_BE_INTEGER_PTBR, input_received=id_lanche)

    # id_lanche is not negative?
    if id_lanche < 0:
        return bad_request(constants.MESSAGE_SHOULD_HAVE_A_VALID_SNACKID_PTBR, input_received=id_lanche)

    # is this a custom snack?
    if id_lanche > 3:

        # custom snacks need the ingredients list
        if request.json is None:
            logger.debug('JSON is empty')
            return bad_request(constants.MESSAGE_EMPTY_JSON_PTBR)
        logger.debug('JSON received {0}'.format(request.json))

        # The list received should only have the pre-defined ingredients
        try:
            validate_payload(request.json)
        except JsonSchemaException as err:
            logger.error('Invalid payload. {0}'.format(err))
            return bad_request(constants.MESSAGE_INVALID_INGREDIENTS_JSON_PTBR)

        snack = Snack(id_lanche, ingredients=request.json)
        Snack.custom_snacks.append(snack)

    # create the order with the given id
    order = Order()
    order.update_order(id_lanche)
    update_order_cache(order)

    return ok({'token': order.token})


@app.route('/api/pedido/de/<token>', methods=['GET'])
def get_order_by_token(token):
    logger.debug("Received request. token {0}".format(token))
    requested_order = None

    for order in Order.orders_cache:
        if order.token == token:
            logger.debug('Order found')
            requested_order = order

    if requested_order is None:
        return bad_request(constants.MESSAGE_ORDER_WITH_INVALID_TOKEN_PTBR.format(token), input_received=token)

    return ok({'pedido': requested_order})


def update_order_cache(order):
    logger.debug('Order information: {0}'.format(order))
    Order.orders_cache.append(order)
    logger.debug('Orders cache updated')
    for order in Order.orders_cache:
        logger.debug(order)


def bad_request(message, input_received=None):
    logger.error("Invalid input received: {0}".format(input_received))
    return jsonify({'erro': message}), HTTPStatus.BAD_REQUEST, constants.JSON_HEADER


def ok(payload):
    logger.debug("Valid request")
    return jsonify(payload), HTTPStatus.OK, constants.JSON_HEADER
