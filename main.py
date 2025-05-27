import utilitiesA as UtilA
def multiplicar(a,b):
    c= a*b
    return c

def main():
    a = 7 
    b = 3
    c = UtilA.sumaA(a, b)
    d= multiplicar(a,b)
    print(f"La suma de {a} y {b} es :{c}")
    print(f"la multiplicación tiene como resultado {d}")

if __name__ == "__main__":
    main()

