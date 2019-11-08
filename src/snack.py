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
        self.price = Ingredient.get_price_by_ingredients_ids_list(ingredients)
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
        if snack_id <= 3:
            for snack in Snack.pre_defined['lanches']:
                if snack['id'] == snack_id:
                    snack['preco'] = Ingredient.get_price_by_ingredients_names_list(snack['ingredientes'])
                    logger.debug('Pre-defined snack: {0}'.format(snack))
                    return snack
        # it is a custom snack!
        for custom_snack in Snack.custom_snacks:
            if custom_snack.snack_id == snack_id:
                snack = {
                    'id': custom_snack.snack_id,
                    'nome': custom_snack.name,
                    'ingredientes': custom_snack.ingredients,
                    'preco': custom_snack.price
                }
                logger.debug('Custom snack: {0}'.format(snack))
                return snack
