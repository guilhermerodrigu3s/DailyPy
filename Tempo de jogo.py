hr_incial=(int(input("Digite o horario inicial: ")))
hr_final=(int(input("Digite o horario final:  ")))

if hr_final > hr_incial:
  res=hr_final - hr_incial
  print(f"Voce jogou por {res} horas")
elif hr_final <= hr_incial:
    res= (24 - hr_incial) + hr_final
    print(f"Você jogou por {res} horas")