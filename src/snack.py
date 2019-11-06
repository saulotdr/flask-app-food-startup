from src.ingredient import Ingredient

class Snack:
    pre_defined = {
        'X-Bacon': {
            'id' : 0,
            'ingredientes': [
                'Pão com gergelim', 'Bacon', 'Hambúrguer de carne', 'Queijo'
            ],
            'preco': Ingredient.pre_defined
        },
        'X-Burguer': {
            'id' : 1,
            'ingredientes': {
                'Pão com gergelim': Ingredient.pre_defined['Pão com gergelim'],
                'Hambúrguer de carne': Ingredient.pre_defined['Hambúrguer de carne'],
                'Queijo': Ingredient.pre_defined['Queijo']
            }
        },
        'X-Egg': {
            'id' : 2,
            'ingredientes': {
                'Pão com gergelim': Ingredient.pre_defined['Pão com gergelim'],
                'Ovo': Ingredient.pre_defined['Ovo'],
                'Hambúrguer de carne': Ingredient.pre_defined['Hambúrguer de carne'],
                'Queijo': Ingredient.pre_defined['Queijo']
            }
        },
        'X-Egg Bacon': {
            'id' : 3,
            'ingredientes': {
                'Pão com gergelim': Ingredient.pre_defined['Pão com gergelim'],
                'Alface': Ingredient.pre_defined['Alface'],
                'Ovo': Ingredient.pre_defined['Ovo'],
                'Bacon': Ingredient.pre_defined['Bacon'],
                'Hambúrguer de carne': Ingredient.pre_defined['Hambúrguer de carne'],
                'Queijo': Ingredient.pre_defined['Queijo']
            }
        }
    }

    @staticmethod
    def get_all_snacks_names():
        snacks = list()
        for k, v in Snack.pre_defined.items():
            snacks.append(k)
        return {'lanches': snacks}

    @staticmethod
    def get_snack_ingredient_and_price_by_id(snack_id):
        pass



