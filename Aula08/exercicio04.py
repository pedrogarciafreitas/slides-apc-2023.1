def main():
    contador_impares = 0
    contador_pares = 0
    while True:
        n = int(input("Escreva um novo valor:"))
        if n >= 0:
            if n % 2 == 0:
                contador_pares += 1
            else:
                contador_impares += 1
        else:
            break
    print(f"Voce digitou {contador_pares} numeros pares")
    print(f"Voce digitou {contador_impares} numeros impares")


if __name__ == "__main__":
    main()