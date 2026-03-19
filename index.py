# Crie um programa que peça o nome de uma pessoa, o curso em que ela estuda e o período atual, e depois mostre todas essas informações em uma frase organizada.

nome = input("Digite o seu nome: ")
curso = input("DIgite qual curso esta realizando: ")
periodo = int(input("Digite o periodo atual do curso: "))

print("\nOla meu nome é {},sou estudante do curso de {} e atualmente estou no {} periodo".format(nome, curso, periodo))