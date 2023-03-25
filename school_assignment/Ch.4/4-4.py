word_list = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
abbreviation_list = []
def abbreviation():
    my_word_list = ['ali', 'ja', 'sam', 'i', 'jucer', 'jeo']#input("줄이고 싶은 말을 쓰시오:").split()
    if my_word_list[0] in word_list:
        word = my_word_list[0][0].upper()
        abbreviation_list.append(word)
    n = len(my_word_list)
    temp_list = my_word_list[:]
    for i in range(n):
        if my_word_list[i] in word_list:
            temp_list.remove(my_word_list[i])
    for j in range(len(temp_list)):
        word = temp_list[j][0].upper()
        abbreviation_list.append(word)
    resoult =''.join(abbreviation_list)
    return resoult

abbreviation()