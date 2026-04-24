variavel3 = 12
variavel4 = 12


def teste(variavel1, variavel2):
    variavel1 -= 10
    variavel2 -= 20
    return variavel1, variavel2


print(variavel3, variavel4)

variavel3, variavel4 = teste(variavel3, variavel4)

print(variavel3, variavel4)