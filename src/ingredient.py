class Ingredient:
    pre_defined = [
        {
            'id': 0,
            'nome': 'Alface',
            'preco': 0.4
        }, {
            'id': 1,
            'nome': 'Bacon',
            'preco': 2
        }, {
            'id': 2,
            'nome': 'Hambúrguer de carne',
            'preco': 3
        }, {
            'id': 3,
            'nome': 'Ovo',
            'preco': 0.8
        }, {
            'id': 4,
            'nome': 'Queijo',
            'preco': 1.5
        }, {
            'id': 5,
            'nome': 'Pão com gergelim',
            'preco': 1
        },

    ]

    @staticmethod
    def get_all_ingredients_names():
        ingredients = list()
        for ingredient in Ingredient.pre_defined:
            ingredients.append(ingredient['nome'])
        return {'ingredientes': ingredients}

    @staticmethod
    def get_all_ingredients_names_list():
        ingredients = list()
        for ingredient in Ingredient.pre_defined:
            ingredients.append(ingredient['nome'])
        return ingredients

    @staticmethod
    def get_price_by_ingredients_list(ingredients):
        price = 0
        for ingredient in ingredients:
            for itens in Ingredient.pre_defined:
                if ingredient in itens['nome']:
                    price = price + itens['preco']
        return price

