def suma(a,b):
    result = [0, 0, 0, 0, 0, 0, 0, 0]
    for x in range (0, 8):
        result[x] = (a[x] + b[x]) % 2

    print(result)

def GF_product_p(a,b):
    aT = -1
    bT = -1

    result = [0] * (8+8+1)

    print(aT)
    print(bT)

    for j in range (0, 8):
        if (a[j] == 1):
            for k in range (0, 8):
                if (b[k] == 1):
                    if (result[j + k] == 0):
                        result[j + k] = 1
                    else:
                        result[j + k] = 0

    print(result)

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
    GF_product_p(a, b)