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
        logger.error('Not a valid integer')
    except ValueError:
        logger.error('Not an integer')
        return bad_request(constants.MESSAGE_INTEGER_ONLY_PTBR, input_received=id_lanche)

    if id_lanche < 0 or id_lanche > 3:
        return bad_request(constants.MESSAGE_INVALID_SNACKID_PTBR, input_received=id_lanche)

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
def create_shopping_cart_with_snackid(id_lanche):
    logger.debug('Received request. id_lanche {0}'.format(id_lanche))

    try:
        id_lanche = int(id_lanche)
    except ValueError:
        logger.error('Not an integer')
        return bad_request(constants.MESSAGE_INTEGER_ONLY_PTBR, input_received=id_lanche)

    if id_lanche < 0:
        logger.error('Not a positive integer')
        return bad_request(constants.MESSAGE_INVALID_SNACKID_PTBR, input_received=id_lanche)

    if id_lanche > 3:
        ingredients = request.json

        if ingredients is None or not ingredients:
            logger.debug('JSON is empty')
            return bad_request(constants.MESSAGE_EMPTY_JSON_PTBR)
        logger.debug('JSON received {0}'.format(ingredients))

        try:
            validate_payload(ingredients)
            logger.debug('Ingredients JSON successfully validated')
        except JsonSchemaException as err:
            logger.error('Invalid payload. {0}'.format(err))
            return bad_request(constants.MESSAGE_INVALID_INGREDIENTS_PTBR)

        snack = Snack(id_lanche, ingredients=ingredients['ingredientes'])
        Snack.custom_snacks.append(snack)

    # create the order with the given id
    order = Order()
    order.update_order(id_lanche)
    update_order_cache(order)

    return ok({'token': order.token})


@app.route('/api/pedido/<token>/<id_lanche>', methods=['PUT'])
def put_snack_in_shopping_cart(token, id_lanche):
    logger.debug('Received request. token {0}, id_lanche {1}'.format(token, id_lanche))

    requested_order = None
    for order in Order.orders_cache:
        if order.token == token:
            logger.debug('order found')
            requested_order = order

    if requested_order is None or not requested_order:
        logger.error('Shopping cart does not exist')
        return bad_request(constants.MESSAGE_INVALID_SHOPPING_CART_PTBR)

    try:
        id_lanche = int(id_lanche)
        logger.debug('Snack ID is an integer')
    except ValueError:
        logger.error('Not an integer')
        return bad_request(constants.MESSAGE_INTEGER_ONLY_PTBR, input_received=id_lanche)

    if id_lanche < 0:
        logger.error('Not a positive integer')
        return bad_request(constants.MESSAGE_INVALID_SNACKID_PTBR, input_received=id_lanche)

    if id_lanche > 3:
        logger.debug('Custom snack requested')
        ingredients = request.json
        if ingredients is None or not ingredients:
            logger.debug('JSON is empty')
            return bad_request(constants.MESSAGE_EMPTY_JSON_PTBR)
        logger.debug('JSON received {0}'.format(ingredients))

        try:
            validate_payload(ingredients)
            logger.debug('Ingredients JSON successfully validated')
        except JsonSchemaException as err:
            logger.error('Invalid payload. {0}'.format(str(err)))
            return bad_request(constants.MESSAGE_INVALID_INGREDIENTS_PTBR)

        snack = Snack(id_lanche, ingredients=ingredients['ingredientes'])
        Snack.custom_snacks.append(snack)

    requested_order.update_order(id_lanche)
    update_order_cache(requested_order)

    return ok({'r': 'Ok', 'token': requested_order.token})


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
    Order.orders_cache.add(order)
    logger.debug('Orders cache updated')
    for order in Order.orders_cache:
        logger.debug(order)


def bad_request(message, input_received=None):
    logger.error("Invalid input received: {0}".format(input_received if input_received is not None else ''))
    return jsonify({'erro': message}), HTTPStatus.BAD_REQUEST, constants.JSON_HEADER


def ok(payload):
    logger.debug("Valid request")
    return jsonify(payload), HTTPStatus.OK, constants.JSON_HEADER
