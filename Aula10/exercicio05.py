# 5. Você sabia que, dependendo do país, existem diferentes modos de escrever
# as datas? Não existe um modo universal em todas as nações para escrever datar
# os dias e anos, porém métodos mais utilizados de acordo com países. Por
# exemplo, aqui no Brasil nós escrevemos dia/mês/ano. Já nos Estados Unidos, o
# correto é escrever mês/dia/ano. Por outro lado, no Japão escrevemos
# ano/mês/dia. Enquanto no Canadá todos esses modos estão certos .
#
# O método aplicado é importante para bancos, para empresas, para calendários
# escolares e para nós organizarmos as nossas férias, porém não existem
# diferenças substanciais entre um modo e outro. Como cada país adota o sistema
# que julga ser mais interessante, é preciso chegar a um consenso global para
# evitar problemas relacionados às datas. Foi assim que chegamos ao ISO 8601,
# emitido pela International Standardization Organization.
#
# A principal característica do formato de data e hora da norma ISO 8601 é que
# a informação da data e da hora seja ordenada a partir do valor mais
# significativo – em outras palavras, do maior ao menor (ano/mês/dia). Hoje,
# existem alguns países que adotaram o ISO 8601 como data oficial para
# facilitar essa padronização, como é o caso do Japão e Coreia do Sul.
#
# Faça um programa que detecte qual o formato da data e a converta para o
# formato ISO 8601. Isto é, se ela tiver no formato US (mes/dia/ano),
# converta-a para ano/mes/dia. Se a data de entrada estiver no formato BR
# (dia/mes/ano), converta-a  para ano/mes/dia. Se ela já tiver no formato ISO,
# apenas imprima na tela. Mas se não for possível determinar se a data está no
# formato BR ou US, imprima a mensagem de erro “Formato de entrada
# indeterminado”.


def print_undetermined_format():
    print("Formato de entrada indeterminado!")


def print_invalid_date():
    print("Data inválida!")


def print_date(date_elements):
    print("/".join(date_elements))


def is_valid_year(year):
    if len(year) == 4:
        return 0 <= int(year) <= 9999
    else:
        return False


def is_valid_month(month):
    if len(month) == 2:
        return 1 <= int(month) <= 12
    else:
        return False


def is_leap_year(year):
    year = int(year)
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def is_valid_day(year, day, month):
    if is_valid_month(month):
        if int(month) == 2:
            end_day = 29 if is_leap_year(year) else 28
            return 1 <= int(day) <= end_day
        elif int(month) in (4, 6, 9, 11):
            return 1 <= int(day) <= 30
        else:
            return 1 <= int(day) <= 31
    else:
        return False


def is_valid_date(year, month, day):
    condition1 = is_valid_year(year) and is_valid_month(month)
    condition2 = is_valid_day(year, day, month)
    return condition1 and condition2


def is_iso_format(date_elements):
    year, month, day = date_elements
    return is_valid_date(year, month, day)


def is_br_format(date_elements):
    day, month, year = date_elements
    return is_valid_date(year, month, day)


def is_us_format(date_elements):
    month, day, year = date_elements
    return is_valid_date(year, month, day)


def br2iso(date_elements):
    day, month, year = date_elements
    return year, month, day


def us2iso(date_elements):
    month, day, year = date_elements
    return year, month, day


def convert_date(date_elements):
    if is_iso_format(date_elements):
        print_date(date_elements)
    elif is_br_format(date_elements) and is_us_format(date_elements):
        day, month, _ = date_elements
        if day == month:
            reordered = br2iso(date_elements)
            print_date(reordered)
        else:
            print_undetermined_format()
    elif is_br_format(date_elements):
        reordered = br2iso(date_elements)
        print_date(reordered)
    elif is_us_format(date_elements):
        reordered = us2iso(date_elements)
        print_date(reordered)
    else:
        print_invalid_date()


def convert(date_elements):
    if len(date_elements) == 3:
        convert_date(date_elements)
    else:
        print_invalid_date()


def main():
    str_date = input("Digite uma data separada por '/': ")
    date_elements = str_date.split("/")
    convert(date_elements)


if __name__ == "__main__":
    main()
