temp=(input("Você vai digitar a temperatura em qual escala (C/F)?"))

if temp == 'F':
  far=(float(input("Digite a temperatura em Farenheit: ")))
  convert_c= 5/9 * (far - 32)
  print(f"Temperatura em CELSIUS: {convert_c}")
elif temp == 'C':
  cel = float(input("Digite a temperatura em Celsius: "))
  convert_f = cel * 1.8 + 32
  print(f"Temperatura em FAHRENHEIT: {convert_f:.2f}")