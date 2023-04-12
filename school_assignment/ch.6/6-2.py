def merge(a,b):
    f = open(b,'w')
    f.close()
    for i in a :
        f = open(b, 'a')
        k = open(i, 'r')
        f.write(k.read())
        f.close()
        k.close()
    with open(b,'r') as f:
        print(f.read())
merge( ["pnu1.txt", "pnu2.txt", "pnu3.txt"], "result.txt" )

merge(["pnu1.txt", "pnu2.txt"], "result.txt")