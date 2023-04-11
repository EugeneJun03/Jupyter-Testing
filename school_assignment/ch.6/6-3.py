import csv

# 3-1
f = open("average-latitude-longitude-countries.csv", "r")
rdr = csv.reader(f)
list1 = []
for line in rdr:
    if line[0] != "ISO 3166 Country Code":
        list1.append((line[0], line[1]))
f.close()
print(list1)

f = open("average-latitude-longitude-countries.csv", "r")
rdr = csv.reader(f)
list2 = []
for line in rdr:
    if line[0] != "ISO 3166 Country Code":
        list2.append((line[0], (float(line[2]), float(line[3]))))
f.close()
print(list2)


#3-2
f = open("average-latitude-longitude-countries.csv", "r")
rdr = csv.reader(f)
n = input()
for line in rdr:
    if line[0] == n:
        print(line[1])
        break
f.close()

