product , unit, price = input().split()
product2, unit2, price2 = input().split()
# integer, integer, float

valor_um = int(unit) * float(price)
valor_dois = int(unit2) * float(price2)

valor_total = float(valor_um + valor_dois)
print("VALOR A PAGAR: R$ %0.2f"%(valor_total))
