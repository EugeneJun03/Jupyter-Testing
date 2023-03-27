contry_capital = {"아이슬란드":"레이캬비크", "터키":"앙카라", "캐나다":"오타와", "뉴질랜드":"웰링턴", "스위스":"베른", "네덜란드":"암스테르담", "그리스":"아테네"}
def contry_capital_game():
    score = 0
    j =0 
    for i in contry_capital.keys():
        k=list(contry_capital.values())
        n = input(i)
        if n == k[j]:
            print("정답입니다.")
            score += 1
            j += 1
        else:
            print("오답입니다.")
            j += 1
    print("총 7 문제 중 수도를 맞춘 정답수는", score,"입니다.")

contry_capital_game()
