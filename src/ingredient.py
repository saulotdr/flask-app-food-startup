class Ingredient:
    pre_defined = {
        'Alface': 0.4,
        'Bacon': 2,
        'Hambúrguer de carne': 3,
        'Ovo': 0.8,
        'Queijo': 1.5,
        'Pão com gergelim': 1,
    }

    @staticmethod
    def get_all_ingredients_names():
        ingredients = list()
        for k, v in Ingredient.pre_defined.items():
            ingredients.append(k)
        return {'ingredientes': ingredients}
