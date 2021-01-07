#선형 검색: 배열에서 검색하는 방법 중 가장 기본적인 알고리즘은 선형 검색입니다.
#원하는 키 값을 가진 원소를 찾을 때까지 앞보터 스캔하여 순서대로 정리하는 알고리즘 (c 에서 했던 bubble sort 와 유사해 보인다)
#배열 스캔 종료조건은 2가지이다 , 검색 성공/실패 이다.
#배열원소의 개소가 n개 이면 조건을 판단하는 평균 횟수는 n/2이다.

from typing import Any, Sequence

def seq_search(a : Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색"""
    i = 0

    while True:
        if i == len(a):
            return -1

        if a[i] == key:
            return i
        i += 1
if __name__ == '__main__':
    num = int(input('Input the number of index: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Input value what you search for: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('There is no index have value')
    else:
        print(f'Value that you are searching for is in x[{idx}].')

#seq_search function은 배열 a에서 key인 원소를 선형 검색하는 함수이다.
#key값이 존재하지 않으면 -1을 return 한다.