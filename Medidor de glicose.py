glic=(float(input("Digite sua medida da glicose:")))

if glic <=100:
    print("Classificação normal:")
elif glic >= 100 and glic <= 140:
    print("Classificação: elevado")
elif glic > 140:
    print("Classificação: diabetes")