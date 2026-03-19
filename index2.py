# Faça um programa que solicite três números inteiros e mostre a soma total entre eles.

numero = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
soma = numero+numero2+numero3

print("\nA soma entre os valores recebidos respectivamente: {},{},{}, resultou em: {}".format(numero, numero2, numero3, soma))