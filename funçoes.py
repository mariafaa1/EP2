import random
def rolar_dados(n):
    lista = []
    i = 0
    while i < n:
        s = random.randint(1,6)
        lista.append(s)

        i+=1

    return lista


