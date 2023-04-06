n = input().split()
sum = 0
for i in n:
    sum += int(i)
cut = sum - 100
flag = False
for j in range(len(n)):
    for k in range(j+1, len(n)):
        if cut == int(n[j]) + int(n[k]):
            del n[k]
            del n[j]
            flag = True
            break
    if flag == True:
        break

n = list(map(int, n))
n.sort()
for l in n:
    print(l)