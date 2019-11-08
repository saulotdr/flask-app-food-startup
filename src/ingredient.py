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
            ing_dict = {
                'id': ingredient['id'],
                'nome': ingredient['nome']
            }
            ingredients.append(ing_dict)
        return {'ingredientes': ingredients}

    @staticmethod
    def get_all_ingredients_ids():
        ids = list()
        for ingredient in Ingredient.pre_defined:
            ids.append(ingredient['id'])
        return ids

    @staticmethod
    def get_price_by_ingredients_names_list(ingredients):
        price = 0
        for ingredient in ingredients:
            for item in Ingredient.pre_defined:
                if ingredient in item['nome']:
                    price = price + item['preco']
        return price

    @staticmethod
    def get_price_by_ingredients_ids_list(ingredients):
        price = 0
        for ingredient in ingredients:
            for item in Ingredient.pre_defined:
                if ingredient == item['id']:
                    price = price + item['preco']
        return price

