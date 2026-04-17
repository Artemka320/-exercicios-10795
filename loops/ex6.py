print("Os 10 primeiros números primos são:")
cont = 0
num = 2

while cont < 10:
    divisores = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1
    if divisores == 2:
        print(num, end=" ")
        cont += 1
    num += 1
print()
