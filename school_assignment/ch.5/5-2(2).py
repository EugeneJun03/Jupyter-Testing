import random

# 가위바위보 승패를 결정하는 함수
def judge(player, computer):
    if player == computer:
        return 0 # 무승부
    elif player == '가위' and computer == '바위':
        return -1 # 패배
    elif player == '바위' and computer == '보':
        return -1 # 패배
    elif player == '보' and computer == '가위':
        return -1 # 패배
    else:
        return 1 # 승리

# 게임 시작
player_score = 0
computer_score = 0
rounds = 0

while player_score < 3 and computer_score < 3:
    print(f"\n{rounds+1}번째 판")
    print(f"현재 스코어: 플레이어 {player_score}점, 컴퓨터 {computer_score}점")

    # 플레이어 입력 받기
    player_choice = input("가위, 바위, 보 중 하나를 선택하세요: ")

    # 컴퓨터 선택
    computer_choice = random.choice(['가위', '바위', '보'])
    print(f"컴퓨터: {computer_choice}")

    # 승패 결정
    result = judge(player_choice, computer_choice)

    if result == 0:
        print("무승부입니다.")
        player_score += 1
        computer_score += 1
    elif result == 1:
        print("플레이어가 이겼습니다!")
        player_score += 1
    else:
        print("컴퓨터가 이겼습니다.")
        computer_score += 1

    rounds += 1

# 최종 스코어 출력
print("\n게임 종료")
print(f"최종 스코어: 플레이어 {player_score}점, 컴퓨터 {computer_score}점")

if player_score > computer_score:
    print("플레이어가 이겼습니다!")
else:
    print("컴퓨터가 이겼습니다.")