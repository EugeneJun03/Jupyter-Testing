def find_most_used_letter():
    word = input("단어를 입력하시오.:")
    word_upper = word.upper()
    word_list = list(word_upper)
    word_set = list(set(word_list))
    cnt = []
    for i in word_set:
        cnt.append(word_list.count(i))
    if cnt.count(max(cnt)) > 1:
        print('?')
    else:
        print(word_set[cnt.index(max(cnt))])
    
find_most_used_letter()