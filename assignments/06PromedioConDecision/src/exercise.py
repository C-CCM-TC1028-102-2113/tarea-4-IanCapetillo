def main():
    #escribe tu código abajo de esta línea
    num = 0
sum = 0
i = 0
prom = 0

while num>=0:
    sum = sum + num
    i += 1
    print("Escriba un número para añadir al promedio")
    num = float(input())


prom = sum/(i-1)


print("El promedio es", prom)

    pass
if __name__=='__main__':
    main()
