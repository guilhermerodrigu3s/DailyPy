vogais='aeiou'

frase=(input("digite sua frase: "))
i=0
for letra in frase:
    if letra in vogais:
      i+=1
      
print(f"Sua frase {frase} tem {i} vogais!")
