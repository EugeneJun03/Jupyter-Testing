def merge(files, file):
    u = open(file, "w")
    for i in range(len(files)):
        n = files[i]
        f = open(str(n), "r")
        for j in f:
            u.write(j)
    f.close()
    u.close()

merge(["pnu1.txt", "pnu2.txt"], "result.txt")