# 3. UnBCab. Você foi contratado para criar um aplicativo de transporte que
# permite a busca por motoristas baseada na localização, oferecendo um serviço
# semelhante ao tradicional táxi, mas onde o custo da passagem é dividido entre
# os passageiros. No seu primeiro dia de trabalho, você ficou encarregado de
# escrever o programa responsavel por calcular o preço da passagem. No modelo
# de negócio da empresa, considera-se o consumo de combustivel por km, o numero
# de passageiros (e a tarifa por passageiro) e a distancia em kms percorrida.
# Nesse modelo, considere que o preço do combustível como sendo R$ 5.00/L, o
# consumo é de 2 L/km, e cada passageiro paga uma taxa mínima de R$ 4.00,
# independente da distância. Além disso, deve-se considerar a taxa da operação
# financeira, que depende do banco do pagador.  Essa taxa é um em número real
# entre 0 (0%) e 1 (100%).Sendo assim, tomando como entrada o número de
# passageiros, a distância do trajeto e a taxa do banco, determine o
# preço da viagem.

CAR_CONSUMPTION = 2
FUEL_PRICE = 5
MINIMAL_USER_FEE = 4

users = int(input("Quantos usuários (1 a 4): "))
distance = float(input("Distância a ser percorrida (em KMs): "))
tax = float(input("Digite a taxa do banco (entre 0 e 1): "))

spent_fuel = distance * CAR_CONSUMPTION
paid_fuel = FUEL_PRICE * spent_fuel

no_tax_price = paid_fuel/users + users * MINIMAL_USER_FEE
final_taxed_price = no_tax_price + tax * no_tax_price

print("O preço final da viagem é: {:.2f}".format(final_taxed_price))