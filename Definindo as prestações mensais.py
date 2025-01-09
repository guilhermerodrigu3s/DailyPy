valor_da_casa = (float(input("Digite o valor da casa: ")))

salario=(float(input("Digite o seu salario: ")))

quant_anos = (float(input("Digite em quantos anos irá pagar: ")))

prest_mensal = valor_da_casa / (quant_anos * 12)

print(f"O valor da prestração mensal é: {prest_mensal}")

porc_salario = salario * 0.3

if prest_mensal <= porc_salario:
  print(f"o valor de sua prestação mensal será {prest_mensal}")
else: print("Empréstimo negado!O valor da prestação mensal excede 30 do seu salário")