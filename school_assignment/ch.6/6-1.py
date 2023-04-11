#가계부 프로그램 1
import datetime
today = datetime.datetime.today()
def make_file1():
    n = int(input("1.'새로 만들기', 2.'가계부 보기', 3.'수입 추가하기', 4.'지출 추가하기' 중 한가지를 선택하시오(번호):"))
    if n == 1:
        f = open("account_book.txt", 'w')
        f.close()
    elif n ==2:
        f = open("account_book.txt", 'r')
        for word in f:
            line = word.strip()
            print(word, end="")
        f.close()
    else:
        f = open("account_book.txt", 'a')
        if n == 3:
            m = input("수입금액을 입력하시오(금액 + 사유):")
            f.write(f'[수입] {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}.{today.microsecond}: {m}\n')
            f.close()
        else:
            m = input("지출금액을 입력하시오(금액 + 사유):")
            f.write(f'[지출] {today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}.{today.microsecond}: {m}\n')
            f.close()
        
make_file1()

# 가계부 프로그램 2
import csv
import datetime
today = datetime.datetime.today()
def make_file2():
    n = int(input("1.'새로 만들기', 2.'가계부 보기', 3.'수입 추가하기', 4.'지출 추가하기' 중 한가지를 선택하시오(번호):"))
    if n == 1:
        f = open("account_book.csv", 'w')
        f.close()
    elif n ==2:
        f = open("account_book.csv", 'r')
        rdr = csv.reader(f)
        for line in rdr:
            print(line)
        f.close()
    else:
        f = open("account_book.csv", 'a', newline="")
        wr = csv.writer(f)
        if n == 3:
            m = input("수입금액을 입력하시오(금액 + 사유):").split()
            a = int(m[0])
            b = m[1]
            u = open("account_book.csv", 'r')
            rdr = csv.reader(u)
            full = 0
            for line in rdr:
                if len(line) > 4:
                    full = int(line[-1])
            full += a
            wr.writerow(['수입', f'{today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}.{today.microsecond}', f'{a}', f'{b}',f'{full}'])
            f.close()
            u.close()
        else:
            m = input("지출금액을 입력하시오(금액 + 사유):").split()
            a = int(m[0])
            b = m[1]
            u = open("account_book.csv", 'r')
            rdr = csv.reader(u)
            full = 0
            for line in rdr:
                if len(line) > 4:
                    full = int(line[4])
            full -= a
            wr.writerow(['지출', f'{today.year}-{today.month}-{today.day} {today.hour}:{today.minute}:{today.second}.{today.microsecond}', f'{a}',f'{b}',f'{full}'])
            f.close()
            u.close()
        
#make_file2() # cvs에 내용을 추가할 때마다 빈 리스트가 추가되는 것은 없애야 함
