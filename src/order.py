from logging import getLogger
from uuid import uuid4
from json import dumps

from src.sale import Sale
from src.snack import Snack

logger = getLogger(__name__)


class Order:
    orders_cache = dict()

    def __init__(self, token, snack_list, total):
        self.token = token
        self.snack_list = snack_list
        self.total = total

    def __init__(self):
        self.token = self.generate_order_token()
        self.snack_list = list()
        self.total = 0

    def update_order(self, snack_id):
        self.snack_list.append(snack_id)
        snack = Snack.get_snack_info_per_id(snack_id)
        self.total += snack['preco'] * Sale.get_discount(snack['ingredientes'])

    def __str__(self):
        return dumps({
            'token': self.token,
            'snack_list': self.snack_list,
            'total': self.total,
        }, indent=4)

    @staticmethod
    def generate_order_token():
        return str(uuid4())

    @staticmethod
    def invalidate_order_cache():
        logger.debug('Invalidating orders cache')
        Order.orders_cache.clear()
