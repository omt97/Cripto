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
    return modul(mult(a, b), div)


def GF_tables():
    print("a")

def GF_product_t(a,b):
    print(a)

def GF_generador():
    pass

def GF_invers(a):
    pass

if __name__ == '__main__':
    a = [1, 1, 1, 0, 1, 0, 1, 0]
    b = [1, 1, 0, 0, 0, 0, 0, 1]
    print(GF_product_p(a, b))