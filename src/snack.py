from src.ingredient import Ingredient


class Snack:
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

    @staticmethod
    def get_all_snacks_names():
        snacks = Snack.pre_defined['lanches']
        snack_list = list()
        for snack in snacks:
            snack_list.append(snack['nome'])
        return {'lanches': snack_list}

    @staticmethod
    def get_snack_ingredients_and_price_by_id(snack_id):
        for snack in Snack.pre_defined['lanches']:
            print(snack)
            if snack['id'] == snack_id:
                snack['preco'] = Ingredient.get_price_by_ingredients_list(snack['ingredientes'])
                return snack
