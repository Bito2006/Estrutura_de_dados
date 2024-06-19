from ex02 import *

def test_extrair_posicoes_pares_impares():
    entrada = [1, 2, 3, 4, 5]
    saida = extrair_posicoes_pares_impares(entrada)

    assert saida == [2, 6, 6, 12, 10]