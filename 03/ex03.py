def gerar_lista(entrada: list) -> list:
    saida = []

    for i, n in enumerate(entrada):
        if i == 0:
            if n % 2 == 0:
                saida.append(n + 2)
            else:
                saida.append(n - 1)

        elif n % 2 == 0:
            saida.append(n + saida[i - 1])


        else:
            saida.append(n - saida[i - 1])

    return saida
