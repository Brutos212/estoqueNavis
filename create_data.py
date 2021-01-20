import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projetonavis.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from projetonavis.produtos.models import Produtos

class Utils:
    """Métodos genéricos."""
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))

class ProdutosClass:
    @staticmethod
    def criar_produtos(produtos):
        Produtos.objects.all().delete()
        aux = []
        for produtos in produtos:
            data = dict(
                produtos=produtos,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            
            obj = Produtos(**data)
            aux.append(obj)
        Produtos.objects.bulk_create(aux)


produtos = (
    "Roupas"
    "Tenis"
    "chinelos"

)

tic = timeit.default_timer()
ProdutosClass.criar_produtos(produtos)

toc = timeit.default_timer()

print("Tempo: ", toc - tic)
