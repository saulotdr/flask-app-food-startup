import logging
from sys import stdout
from os import environ as env

""" Constants """
JSON_HEADER = {'Content-Type': 'application/json'}
MESSAGE_SHOULD_BE_INTEGER_PTBR = '<id_lanche> deve ser um número inteiro'
MESSAGE_SHOULD_HAVE_A_VALID_SNACKID_PTBR = '<id_lanche> deve ser um id, dentre os quais: {0, 1, 2, 3}'
MESSAGE_INVALID_INGREDIENTS_JSON_PTBR = 'JSON inválido. o formato deve ser {"ingredientes": [ing1, ing2]}'
MESSAGE_EMPTY_JSON_PTBR = 'JSON vazio ou nulo'
MESSAGE_ORDER_WITH_INVALID_TOKEN_PTBR = 'Order with token {0} does not exist'

""" Environment variables """
PRETTY_PRINT = env['PRETTY_PRINT'] if 'PRETTY_PRINT' in env else False
DEBUG_LEVEL = env['DEBUG_LEVEL'] if 'DEBUG_LEVEL' in env else logging.ERROR

""" Root logging basic configuration """
logging.basicConfig(level=DEBUG_LEVEL,
                    stream=stdout,
                    format='%(asctime)s [%(levelname)s] - %(funcName)s: %(message)s'
                    )
