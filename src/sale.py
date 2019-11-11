class Sale:
    pre_defined = {
        'promocoes': [
            {
                'id': 0,
                'nome': 'Light',
                'descricao': "Se o lanche tem alface e não tem bacon, ganhe 10% de desconto."
            }, {
                'id': 1,
                'nome': 'Muita carne',
                'descricao': "A cada 3 porções de carne o cliente só paga 2. Se o lanche tiver 6 porções, o cliente "
                             "pagará 4. "
            }, {
                'id': 2,
                'nome': 'Muito queijo',
                'descricao': "A cada 3 porções de queijo o cliente só paga 2. Se o lanche tiver 6 porções, "
                             "o cliente pagará 4. "
            }
        ]
    }

    @staticmethod
    def get_all_sales():
        return Sale.pre_defined

    @staticmethod
    def get_discount(ingredients):
        total = {ing: ingredients.count(ing) for ing in ingredients}
        lettuce, bacon, meat, cheese = 0, 1, 2, 4

        if meat in total and total[meat] > 3 or cheese in total and total[cheese] > 3:
            return 0.666667
        if lettuce in total and bacon not in total:
            return 0.90
        return 1
