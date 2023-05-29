# Você foi contratado para ser desenvolvedor de software de um banco. Em
# sua primeira atribuição, ficou responsável por escrever um programa que
# calcule e entregue as notas de um saque. Seu programa deve receber como
# entrada um valor a ser sacado e retornar a quantidade de notas de R$100,
# R$50, R$20, R$10, R$2 e R$1 necessárias para efetuar o saque. Considere que
# seu programa está em processo de homologação e, por isso, não irá
# disponibilizar as notas fisicamente, mas exibirá na tela do time de testes a
# quantidade de notas que ele irá retornar. Seguem os exemplos abaixo:
# 
# Exemplo 01:
# 
# Valor do saque: R$ 120
# Entregue 1 nota de R$ 100,00
# Entregue 1 nota de R$ 20,00
# 
# 
# Exemplo 02
# 
# Valor do saque: R$ 4
# Entregue 2 notas de R$ 2,00
# 
# 
# Exemplo 03:
# 
# Valor do saque R$ 666
# Entregue 6 notas de R$ 100,00
# Entregue 1 notas de R$ 50,00
# Entegue 1 nota de R$ 10,00
# Entregue 3 nota de R$ 2,00


def get_format_string(bills):
    if bills == 1:
        return "Entregue {bills} nota de R$ {buck:.2f}"
    else:
        return "Entregue {bills} notas de R$ {buck:.2f}"


def pretty_print_output(counted_bills):
    for (buck, bills) in counted_bills.items():
        fmt_str = get_format_string(bills)
        out = fmt_str.format(bills=bills, buck=buck)
        print(out)


def count_bucks(amount):
    bucks = (100, 50, 20, 10, 2, 1)
    counter = {}
    for buck in bucks:
        counter[buck] = amount // buck
        amount = amount % buck
    return counter


def get_deliverable_bucks(counted_bucks):
    return {buck:bills for (buck, bills) in counted_bucks.items() if bills > 0}


def get_withdraw():
    return int(float(input("Valor do saque: R$ ")))


def main():
    value = get_withdraw()
    counted_bucks = count_bucks(value)
    only_nonzero_bills = get_deliverable_bucks(counted_bucks)
    pretty_print_output(only_nonzero_bills)
    


if __name__ == "__main__":
    main()