while True:
    num = int(input("Introduza um número entre 1 e 100: "))
    if 1 <= num <= 100:
        print(f"Número válido: {num}")
        break
    else:
        print("Valor inválido! Tente novamente.")
