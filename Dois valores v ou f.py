pnum = (int(input("Digite o primeiro valor: ")))
snum = (int(input("Digite o segundo valor: ")))

if pnum > snum:
  print("O primeiro valor é maior")
elif pnum<snum:
  print("O segundo valor é maior")
elif  pnum == snum:
  print("Não existe valor maior, ambos são iguais")