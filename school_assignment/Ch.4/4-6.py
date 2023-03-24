import decimal
decimal.Decimal(0.1)

i = 0
res = 0

while i <100:
    res += 0.1
    i += 1
    d_res = decimal.Decimal(res)
res