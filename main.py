import utilitiesA as UtilA
def resta(a,b):
    d = a - b
    return d

def main():
    a = 7 
    b = 3
    c = UtilA.sumaA(a, b)
    d = resta(a,b)
    print(f"La suma de {a} y {b} es :{c}")
    print(f"Resultado de resta: {d}")


    
if __name__ == "__main__":
    main()


