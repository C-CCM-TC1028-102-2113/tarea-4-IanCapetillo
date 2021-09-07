def main():
    #escribe tu código abajo de esta línea
    num = 0
i = 0

print("Please type the number")
num = int(input())

while i != num:
    i = i + 1
    if (i%2) == 0:
        print(str(i) + "-%")
    elif (i%2)!=0:
        print(str(i) + "-#")
    else:
        print("Error")
    pass

if __name__=='__main__':   
    main()
