n = list(range(1, 10001))
set_num = set()
for i in range(1, 10001):
    d = i
    i_list = list(str(i))
    for j in i_list:
        d += int(j)
    if d <= 10000:
        set_num.add(d)

for i in list(set_num):
    n.remove(i)
for k in n:
    print(k)