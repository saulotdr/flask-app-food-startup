from logging import getLogger
from src.ingredient import Ingredient

logger = getLogger(__name__)


class Snack:
    custom_snacks = list()
    pre_defined = {
        'lanches': [
            {
                'id': 0,
                'nome': 'X-Bacon',
                'ingredientes': ['Pão com gergelim', 'Bacon', 'Hambúrguer de carne', 'Queijo']
            },
            {
                'id': 1,
                'nome': 'X-Burguer',
                'ingredientes': ['Pão com gergelim', 'Hambúrguer de carne', 'Queijo']
            },
            {
                'id': 2,
                'nome': 'X-Egg',
                'ingredientes': ['Pão com gergelim', 'Ovo', 'Hambúrguer de carne', 'Queijo']
            },
            {
                'id': 3,
                'nome': 'X-Egg Bacon',
                'ingredientes': ['Pão com gergelim', 'Alface', 'Ovo', 'Bacon', 'Hambúrguer de carne', 'Queijo']
            }
        ]
    }

    def __init__(self, snack_id, ingredients=None):
        self.snack_id = snack_id
        self.name = 'Personalizado {0}'.format(snack_id)
        self.ingredients = ingredients

    @staticmethod
    def get_all_snacks_names():
        snacks = Snack.pre_defined['lanches']
        snack_list = list()
        for snack in snacks:
            snack_list.append(snack['nome'])
        return {'lanches': snack_list}

    @staticmethod
    def get_snack_info_per_id(snack_id):
        # is this a predefined snack?
        if snack_id < 3:
            for snack in Snack.pre_defined['lanches']:
                if snack['id'] == snack_id:
                    snack['preco'] = Ingredient.get_price_by_ingredients_list(snack['ingredientes'])
                    return snack
        # it is a custom snack!
        for custom_snack in Snack.custom_snacks:
            if custom_snack.snack_id == snack_id:
                return {
                    'id': custom_snack.id,
                    'nome': custom_snack.name,
                    'ingredientes': custom_snack.ingredients,
                    'preco': Ingredient.get_price_by_ingredients_list(custom_snack.ingredients)
                }
        # snack id is missing from cache
        logger.error("Snack is missing from cache")
        return None
