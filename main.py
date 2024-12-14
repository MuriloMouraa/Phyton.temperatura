print("Convertor de temperatura, digite abaixo qual temperatura está:")

esc1 = float(input())

print("Digite a escala dessa temperatura: (C, F ou K)")

esc2 = str(input())

print("Qual escala quer converter? (C, F ou K)")

esc3 = str(input())

if esc2 == "C" and esc3 == "F":
 print("%.2f" % ((esc1 * 9/5) + 32))
elif esc2 == "C" and esc3 == "K":
  print("%.2f" % (esc1 - 273.15))
elif esc2 == "F" and esc3 == "C":
  print("%.2f" % ((esc1 - 32) * 5/9))
elif esc2 == "K" and esc3 == "C":
  print("%.2f" % (esc1 + 273.15))
elif esc2 == "F" and esc3 == "K":
  print("%.2f" % ((esc1 - 32) * 5/9 + 273.15))
elif esc2 == "K" and esc3 == "F":
  print("%.2f" % ((esc1 -273.15) * 9/5 + 32))
else:
  print("Escala invalida")
  