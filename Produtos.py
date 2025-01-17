p_produto = (float(input("Digite o preço unitário do produto")))
q=(int(input("Digite a quantidade de produto comprada: ")))
d=(float(input("Digite quanto irá pagar: ")))
vlr_total = q * p_produto
troco = d - vlr_total

if d < vlr_total :
  print("Cartão não autorizado")
else:


  print(f"Preço unitario do produto: {p_produto}")
  print(f"Quantidade comprada: {q}")
  print(f"Dinheiro recebido: {d}")
  print(f"Troco: {troco}")