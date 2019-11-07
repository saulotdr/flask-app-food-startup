from logging import getLogger
from uuid import uuid4
from json import dumps

from src.sale import Sale
from src.snack import Snack

logger = getLogger(__name__)


class Order:
    orders_cache = list()

    def __init__(self):
        self.token = self.generate_order_token()
        self.snack_list = list()
        self.subtotal = 0

        self.total = 0

    def update_order(self, snack_id):
        self.snack_list.append(snack_id)
        snack = Snack.get_snack_info_per_id(snack_id)
        if snack is None:
            self.invalidate_order_cache()
        self.subtotal += snack['preco'] -
        self.discount = Sale.get_discount(snack['ingredientes'])

    def __str__(self):
        order = {
            'token': self.token,
            'snack_list': self.snack_list,
            'total': self.total,
            'discount': self.total
        }
        return dumps(order, indent=4)

    @staticmethod
    def generate_order_token():
        return str(uuid4())

    @staticmethod
    def invalidate_order_cache():
        logger.debug('Invalidating orders cache')
        Order.orders_cache.clear()


