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
                'ingredientes': "A cada 3 porções de queijo o cliente só paga 2. Se o lanche tiver 6 porções, "
                                "o cliente pagará 4. "
            }
        ]
    }

    @staticmethod
    def get_all_sales():
        return Sale.pre_defined

    @staticmethod
    def get_discount(ingredients):
        if ingredients.count()

