# 09 Área de un Rectángulo
# Claudia Imazul Espinosa Amezcua
# A01176716
# TC1028.37 

def area(base,altura):
    return base*altura

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))

    r = area(b,a)

    print("El área del rectángulo es:",r)

if __name__=='__main__':
    main()
