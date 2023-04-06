n =  int(input())
num = set()
for i in range(1,n+1):
    if n//i == 0:
        num.append(i)
num_list = list(num)
sum = 0
for i in num_list:
    sum += int(i)
print(sum)