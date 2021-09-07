
def main():
    #Escribe tu código debajo de esta línea
    height = 0
i = 1
j = 0
k = 0
spaces = ""
asterisks = ""

print("Please type the height of the triangle:")
height = int(input())


for i in range(-1, height, 1):
    for j in range(height, i, -1):
        spaces = (spaces + " ")
    for k in range (i, height, 1):
        asterisks = (asterisks + "*")
    
    print(spaces + asterisks)

    pass


if __name__=='__main__':
    main()
