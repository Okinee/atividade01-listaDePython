# Faça um programa que peça o valor de um produto e o percentual de desconto, calculando quanto o produto passara a custar apos o desconto

produto = float(input("Digite o valor do produto: "))
percentDesconto = float(input("Digite o valor do desconto: "))

desconto = produto * percentDesconto

valorFinal = produto - desconto

print("De acordo com o valor do produto: {} e o percentual de desconto: {}, serão economizados {}, sendo o valor do produto com desconto: {}".format(produto, percentDesconto, desconto, valorFinal))


