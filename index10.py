# Crie um programa que peça o nome do aluno e três notas, calcule a media final e mostre uma mensagem com o nome do aluno e sua média.

notaFinal = 0
nome = input("Digite seu nome: ")
nota1 = int(input("Digite sua primeira nota: "))
notaFinal += nota1
nota2 = int(input("Digite sua segunda nota: "))
notaFinal += nota2
nota3 = int(input("Digite sua terceira nota: "))
notaFinal += nota3

media = notaFinal/3

print("De acordo com as suas três notas: {}, {}, {}, a média final foi: {:.2}".format(nota1, nota2, nota3, media))
