
def main():
    inicio = 1000
    fim = 9999
    numero = inicio
    while numero <= fim:
        numero_as_str = str(numero)
        primeira_dezena = int(numero_as_str[0:2])
        segunda_dezena = int(numero_as_str[2:4])
        soma = primeira_dezena + segunda_dezena
        quadrado_da_soma = soma * soma
        if quadrado_da_soma == numero:
            out = (numero, primeira_dezena, segunda_dezena, quadrado_da_soma)
            print("N=%d, N1=%d, N2=%d, soma2=%d" % out)
        numero += 1


if __name__ == "__main__":
    main()