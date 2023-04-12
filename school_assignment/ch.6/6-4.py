# 4-1
import csv
f = open("6-4.txt", "r")
rdr = csv.reader(f)
sum1 = 0
sum2 = 0
year = 2010
for line in f:
    linelist = line.strip()
    line1 = linelist[0:6]
    line2 = linelist[-5:]
    if int(line1[0:4]) == year:
        if str(line1[4:]) == '01' or str(line1[4:]) == '02':
            sum1 += float(line2)
        elif str(line1[4:]) == '07' or str(line1[4:]) =='08':
            sum2 += float(line2)
    else:
        ans1 = sum1/2
        ans2 = sum2/2
        print(year, ans1, "/", ans2)
        year += 1
        sum1 = 0
        sum2 = 0
        sum1 += float(line2)
ans1 = sum1/2
ans2 = sum2/2
print(year, ans1, "/", ans2)

# 4-2
import csv
f = open("tpmon.csv", "w", newline="")
u = open("6-4.txt", "r")
wr = csv.writer(f)
year = 2010
list3 = []
for line in u:
    linelist = line.strip()
    line1 = linelist[0:6]
    line2 = linelist[-5:]
    if int(line1[0:4]) == year:
        list3.append(line2)
    else:
        a = [year]
        a.extend(list3)
        wr.writerow(a)
        year += 1
        list3 = []
        list3.append(line2)
a = [year]
a.extend(list3)
wr.writerow(a)
f.close()
u.close()
f = open("tpmon.csv", "r")
wr = csv.reader(f)
for line in wr:
    print(line)
f.close()