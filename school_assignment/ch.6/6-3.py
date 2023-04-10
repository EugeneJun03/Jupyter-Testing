import csv
f = open("average-latitude-longitude-countries.csv", "r")
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close