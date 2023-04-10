#가계부 프로그램 1
import datetime
today = datetime.datetime.today()
def make_file():
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
        
make_file()