#  Faça um programa que peça o salário de um funcionário e mostre quanto ele receberá caso tenha um aumento de 15%.

salario = float(input("Digite o valor do seu salario: "))
aumento = salario*0.15
novoSalario = salario+aumento

print("\nDe acordo com o salario recebido de: R${} reais, o aumento sera de: R${} reais, resultando em um salario de: R${} reais".format(salario, aumento, novoSalario))