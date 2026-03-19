#  Crie um programa que peça ao usuário a quantidade de quilômetros percorridos e a quantidade de litros de combustível gastos, e depois mostre o consumo médio do veículo.

distancia = float(input("Digite a quantidade de quilometros percorridos: "))
combustivel = float(input("Digite a quantidade de litros de combustivel gastos: "))

consumoMedio = distancia/combustivel

print("\nDe acordo com a distancia: {}, e a quantidade de combustivel: {}, o consumo médio resultou em: {}".format(distancia,combustivel,consumoMedio))