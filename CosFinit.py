import math
from time import time


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
    return decimal(modul(mult(a, b),div))


def GF_tables():
    TabExp = [0]*256
    TabLog = [0]*256
    TabExp[0] = 0x01
    for i in range (1, 256):

        TabExp[i] = GF_product_p(binario(TabExp[i - 1]), binario(0x03))
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
    x = GF_tables()
    return (x[0][(x[1][decimal(a)] + x[1][decimal(b)]) % 255])

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
            power = decimal(GF_product_p(binario(power), binario(a)))
            contador = contador + 1

        if (contador == 255): generadores.append(a)

    return generadores

def GF_invers(a):
    x = GF_tables()
    if a == 0x00: return 0x00
    else: return (x[0][(255 - x[1][a & 0xff]) & 0xff])


def decimal(a):
    result = 0
    for i in range(0, len(a)):
        if(i == 0): result = result + a[i]
        else: result = result + (a[i]*2)**i
    return result


if __name__ == '__main__':
    a = [1, 1, 1, 0, 1, 0, 1, 0]
    b = [1, 1, 0, 0, 0, 0, 0, 1]


    InTime = time()
    x = GF_product_p(a, binario(0x02))
    print("Time product_p02 -> ", end="")
    print((InTime - time()))
    print("Product_p02 -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x02))
    print("Time product_p02 -> ", end="")
    print((InTime - time()))
    print("Product_p02 -> ", end="")
    print(x)

    InTime = time()
    x = GF_product_p(a, binario(0x03))
    print("Time product_p03 -> ", end="")
    print((InTime - time()))
    print("Product_p03 -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x03))
    print("Time product_p03 -> ", end="")
    print((InTime - time()))
    print("Product_p03 -> ", end="")
    print(x)

    InTime = time()
    x = GF_product_p(a, binario(0x09))
    print("Time product_p09 -> ", end="")
    print((InTime - time()))
    print("Product_p09 -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x09))
    print("Time product_p09 -> ", end="")
    print((InTime - time()))
    print("Product_p09 -> ", end="")
    print(x)

    InTime = time()
    x = GF_product_p(a, binario(0x0b))
    print("Time product_p0B -> ", end="")
    print((InTime - time()))
    print("Product_p0B -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x0b))
    print("Time product_p0B -> ", end="")
    print((InTime - time()))
    print("Product_p0B -> ", end="")
    print(x)

    InTime = time()
    x = GF_product_p(a, binario(0x0d))
    print("Time product_p0D -> ", end="")
    print((InTime - time()))
    print("Product_p0D -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x0d))
    print("Time product_p0D -> ", end="")
    print((InTime - time()))
    print("Product_p0D -> ", end="")
    print(x)

    InTime = time()
    x = GF_product_p(a, binario(0x0e))
    print("Time product_p0E -> ", end="")
    print((InTime - time()))
    print("Product_p0E -> ", end="")
    print(x)
    InTime = time()
    x = GF_product_t(a, binario(0x0e))
    print("Time product_p0E -> ", end="")
    print((InTime - time()))
    print("Product_p0E -> ", end="")
    print(x)