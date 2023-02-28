"""네임스페이스(Namespace) - 네임스페이스는 특정이름이 유일하고, 
다른 네임스페이스레서의 같은 이름과 관계가 없는 것을 말한다.
각 함수는 자신의 네임스페이스를 정의한다."""

"""메인프로그램은 전역 네임스페이스를 정의하기 때문에 
이 네임스페이스의 변수들은 전역 변수이다."""

#ex)1 전역변수 구하기
animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)
"""
>>> print('at the top level:', animal)
at the top level: fruitbat
>>> print_global()
inside print_global: fruitbat"""

# 함수에서 전역변수의 값을 바꾸려 하면 오류가 일어난다.
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the hage:', animal)
""">>> change_and_print_global()  
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in change_and_print_global
UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value"""

#ex)2 함수내에 있는 지역변수 구하기 + 지역변수는 함수를 실행하고 사라진다.
def change_local():
    animal = 'wambat'
    print('inside change_local:', animal, id(animal))
"""
>>> change_local()
inside change_local: wambat 2458552561392
>>> animal
'fruitbat'
>>> id(animal)
2458552561264
"""

# 즉, 위의 결과로 같은 이름인 animal이라는 변수임에도 global과 local이라는 차아 때문에 id가 다르다.
# 그래서 함수내에서 전역변수를 사용하기 위해서는 global이라는 키워드를 사용하여 명시해 주어야 한다.
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
"""
>>> animal
'frutbat'
>>> change_and_print_global()
inside change_and_print_global: wombat
>>> animal
'wombat'"""

"""네임스페이스의 내용에 접근하기!
사용함수:
    1.locals() - 로컬 네임스페이스의 내용이 담긴 딕셔너리를 반환한다.
    2.globals() - 글로벌 네임스페이스의 내용이 담긴 딕셔너리를 반환한다."""
'''
>>> animal
'fruitbat'
'''
def change_local():
    animal = 'wombat'
    print('locals:', locals())
'''
>>> animal
'fruitbat'
>>> change_local()
locals: {'animal': 'wombat'}
>>> print('globals:', globals())
globals: {'__name__': '__main__', '__doc__': None, '__package__': None, 
'__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, 
'__builtins__': <module 'builtins' (built-in)>, 'change_and_print_global': 
<function change_and_print_global at 0x0000023C6D278A40>, 'change_local': <function change_local at 0x0000023C6D278B80>, 
'animal': 'fruitbat'}
>>> animal
'fruitbat'
'''