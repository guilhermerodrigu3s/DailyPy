sal=(float(input("Digite o salário da pessoa: ")))
if sal <=1000:
  porcentagem=0.20
  aumento=porcentagem*sal
  novo_sal=aumento+sal
  print(f"Novo salário: {novo_sal}")
  print(f"Aumento= {aumento}")
  print(f"Porcentagem: 20% ")
elif  1000 <= sal <= 3000:
  porcentagem=0.15
  aumento=porcentagem*sal
  novo_sal=aumento+sal
  print(f"Novo salário: {novo_sal}")
  print(f"Aumento= {aumento}")
  print(f"Porcentagem: 15% ")
elif  3000 <= sal <= 8000:
  porcentagem=0.1
  aumento=porcentagem*sal
  novo_sal=aumento+sal
  print(f"Novo salário: {novo_sal}")
  print(f"Aumento= {aumento}")
  print(f"Porcentagem: 10% ")
elif  sal > 8000:
  porcentagem=0.05
  aumento=porcentagem*sal
  novo_sal=aumento+sal
  print(f"Novo salário: {novo_sal}")
  print(f"Aumento= {aumento}")
  print(f"Porcentagem: 5% ")