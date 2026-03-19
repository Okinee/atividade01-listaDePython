# Elabore um programa que peça ao usuario uma temperatura em graus Celsius e mostre o valor correspondente em Fahrenheit

temperaturaCelsius = int(input("Digite o valor da temperatura em Celsius: "))

celsiusParaFahrenheit = (temperaturaCelsius*1.8) + 32

print("De acordo com a temperatura em Celsius: {}, a temperatura em fahrenheit vai ser de: {} Fahrenheit".format(temperaturaCelsius, celsiusParaFahrenheit)


