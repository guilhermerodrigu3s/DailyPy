#descobrindo decimo termo da pa
a1=(int(input("Digite o primeiro termo da PA")))

r= (int(input("Digite a razão da pa")))

dec=a1+(10 - 1)* r

for c in range (a1,dec,r):
  print(c)