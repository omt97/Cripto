import math


def suma(a,b):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range (0, 8):
        result[x] = (a[x] + b[x]) % 2

    print(result)


def mult(a, b):
    result = [0] * (8 + 8 + 1)

    for j in range(0, len(a)):
        if (a[j] == 1):
            for k in range(0, len(b)):
                if (b[k] == 1):
                    if (result[j + k] == 0):
                        result[j + k] = 1
                    else:
                        result[j + k] = 0

    return result

def modul(a, b):
    i = 0
    x = len(a)-1
    while i == 0:
        if (a[x] == 1): i = 1
        else: x = x-1

    if (x < 8): return a
    else:
        multi = [0]*(x-8+1)
        multi[x-8] = 1
        multi = mult(multi, b)
        for j in range (0, len(a)):
            a[j] = (a[j]+multi[j])%2
        return modul(a, b)

def GF_product_p(a,b):
    div = [1, 1, 0, 1, 1, 0, 0, 0, 1]
    return modul(mult(a, b),div)


def GF_tables():
    TabExp = [0]*256
    TabLog = [0]*256
    TabExp[0] = 0x01
    for i in range (1, 256):

        TabExp[i] = normal(GF_product_p(binario(TabExp[i - 1]), binario(0x03)))
        TabLog[TabExp[i] & 0xff] = i

    return (TabExp, TabLog)

def binario(a):
    result = [0]*8
    for i in range (0,8):
        b = a%2
        result[i] = int(b)
        a = a/2

    return result


def GF_product_t(a,b):
    print(a)

def GF_generador():
    tabs = GF_tables()
    generadores = []
    generadores = list()
    contador = 0
    a = 0
    power = 0
    for i in range (0, 256):
        a = tabs[0][i]
        power = a
        contador = 1
        while power != 0x01:
            power = normal(GF_product_p(binario(power), binario(a)))
            contador = contador + 1

        if (contador == 255): generadores.append(a)

    return generadores

def GF_invers(a):
    pass


def normal(a):
    result = 0
    for i in range(0, 13):
        if(i == 0): result = result + a[i]
        else: result = result + (a[i]*2)**i
    return result


if __name__ == '__main__':
    print(GF_generador())
    a = [1, 1, 1, 0, 1, 0, 1, 0]
    b = [1, 1, 0, 0, 0, 0, 0, 1]
    print(normal(GF_product_p(binario(0x97), binario(0x0E))))
    x = GF_tables()
    print(x[0])
    print(x[1])
    print(x[0][(x[1][0x97]+x[1][0x0E]) % 255])
