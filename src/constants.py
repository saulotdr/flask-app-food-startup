import logging
from sys import stdout
from os import environ as env

from src.ingredient import Ingredient

""" Constants """
JSON_HEADER = {'Content-Type': 'application/json'}
MESSAGE_INTEGER_ONLY_PTBR = '<id_lanche> deve ser um número inteiro'
MESSAGE_INVALID_SNACKID_PTBR = '<id_lanche> deve ser um id, dentre os quais: {0, 1, 2, 3}'
MESSAGE_INVALID_INGREDIENTS_PTBR = 'JSON inválido. o formato deve ser {0}'.format(Ingredient.get_all_ingredients_ids())
MESSAGE_EMPTY_JSON_PTBR = 'JSON vazio ou nulo'
MESSAGE_ORDER_WITH_INVALID_TOKEN_PTBR = 'Pedido com o token {0} não existe'
MESSAGE_INVALID_SHOPPING_CART_PTBR = 'Carrinho de compras não existe'

""" Environment variables """
PRETTY_PRINT = env['PRETTY_PRINT'] if 'PRETTY_PRINT' in env else False
LOGGING_LEVEL = env['LOGGING_LEVEL'] if 'LOGGING_LEVEL' in env else logging.ERROR

""" Root logging basic configuration """
logging.basicConfig(level=LOGGING_LEVEL,
                    stream=stdout,
                    format='%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s'
                    )
