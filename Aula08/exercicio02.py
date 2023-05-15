def main():
    soma = 0
    n = 0
    while n != -1:
        n = int(input("Escreva um novo valor:"))
        soma += n
    print(f"O somatorio dos numeros digitados é {soma}")    


if __name__ == "__main__":
    main()