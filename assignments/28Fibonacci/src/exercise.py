
def main():
    #escribe tu código abajo de esta línea
    i = 0
j = 1
k = 1
num = 0
num_control = 0

print("Introduzca el número de la serie de fibonacci que quiere conocer")
num = int(input())

for num_control in range(3, (num+1), 1):
    i = j + k
    k = j
    j = i

if num == 0:
    print("0")
elif num == 1:
    print("1")
elif num == 2:
    print("1")
elif num == 3:
    print("2")
else:
    print(i)
    pass

if __name__=='__main__':
    main()
