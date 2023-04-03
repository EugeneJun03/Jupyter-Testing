import random
list_game = ["가위", "바위", "보"]
def game():
    print("===가위/바위/보 게임을 시작합니다.===")
    print("===5판 3선승제입니다.")
    a = 0
    b = 0
    for i in range(1, 6):
        print(f"==={i}번째 판===")
        n = int(input("1.가위 2.바위 3.보 >> "))
        you = str(list_game[n-1])
        print("  나:", you)
        computer = random.choice(list_game)
        computer_n = list_game.index(computer) + 1
        print("  컴퓨터:", computer)
        if n == 1:
            if computer_n == 1:
                a += 1
                b += 1
                print("현재 스코어:",a,":",b)
            elif computer_n == 2:
                b += 1
                print("현재 스코어:",a,":",b)
            else:
                a += 1
                print("현재 스코어:",a,":",b)
        elif n == 2:
            if computer_n == 2:
                a += 1
                b += 1
                print("현재 스코어:",a,":",b)
            elif computer_n == 3:
                b += 1
                print("현재 스코어:",a,":",b)
            else:
                a += 1
                print("현재 스코어:",a,":",b)
        else:
            if computer_n == 3:
                a += 1
                b += 1
                print("현재 스코어:",a,":",b)
            elif computer_n == 1:
                b += 1
                print("현재 스코어:",a,":",b)
            else:
                a += 1
                print("현재 스코어:",a,":",b)
        if a == 3 or b == 3:
            break
    if a == 3:
        print("당신이 이겼습니다!")
    else:
        print("당신이 졌습니다!")
game()





