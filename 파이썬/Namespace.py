"""네임스페이스(Namespace) - 네임스페이스는 특정이름이 유일하고, 
다른 네임스페이스레서의 같은 이름과 관계가 없는 것을 말한다.
각 함수는 자신의 네임스페이스를 정의한다."""

"""메인프로그램은 전역 네임스페이스를 정의하기 때문에 
네임스페이스의 변수들은 전역 변수이다."""

#ex)1 전역변수 구하기
"""
>>> def print_global():
...     print('inside print_global:', animal)
...
>>> print('at the top level:', animal)
at the top level: fruitbat
>>> print_global()
inside print_global: fruitbat"""