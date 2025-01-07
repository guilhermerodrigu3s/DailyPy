##Faça um programa que converta uma temperatura de Celsius para Fahrenheit e vice-versa.
#Fórmulas:
#Fahrenheit para Celsius: C = (F - 32) * 5/9
#Celsius para Fahrenheit: F = C * 9/5 + 32
#Desafio extra: Permita converter também para Kelvin.

#inserindo a temperatura em celsius

temp_em_celcius = (int(input("Insira aqui o valor em Celcius")))

##aplicando a formula
Fahrenheit = temp_em_celcius * 9/5 + 32

#exibindo o calculo para o úsuario
print(f"A temperatura em celcius é {temp_em_celcius}C, convertida para Farenheit é : {Fahrenheit}F  ")


####Convertendo a temperatura para Kelvin###


#declarando a variavel#
Kelvin= temp_em_celcius + 273,15

#exibindo ao usuario#
print(f"A temperatura em celcius é = {temp_em_celcius}°C, convertida para Farenheit é = {Fahrenheit}°F, já em Kelvin é = {Kelvin}K  ")




