print("Digite 10 números:")
for i in range(1, 11):
    num = int(input(f"{i}º número: "))
    if num % 2 == 0:
        print(f"{num} → PAR")
    else:
        print(f"{num} → ÍMPAR")
