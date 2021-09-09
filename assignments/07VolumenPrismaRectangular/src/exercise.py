# 07 Volúmen de un Prisma Rectangular
# Claudia Imazul Espinosa Amezcua
# A01176716
# TC1028.37 

# Escribe aquí tus funciones...

def volumen_prisma(x, y, z):
    return x * y * z

def main():
    #escribe tu código abajo de esta línea
    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = volumen_prisma(b,a,p)

    print("El volumen del prisma es:",r)

if __name__=='__main__':
    main()
