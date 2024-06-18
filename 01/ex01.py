def extrair_posicoes_pares(entrada: list) -> list:
    saida = []

# i = posição
# n = valor
    for i, n in enumerate(entrada):
        if i % 2 == 0:
            saida.append(n)


# # outra forma
#
#     for i in range(0, len(entrada), 2):
#         saida.append(entrada[i])
    return saida