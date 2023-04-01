n = list(range(1, 10001))

for i in range(1, 10001):
    d = i
    i_list = list(str(i))
    for j in i_list:
        d += int(j)
    if d <= 10000:
        n.remove(d)

for k in n:
    print(n)