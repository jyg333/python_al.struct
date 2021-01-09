# for 문으로 작성한 성형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a : Sequence, key: Any) ->int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1 # searching fail return -1

if __name__ == '__main__':
    num = int(input('Input the number of index: '))
    x = [None] * num  #값이 존재하지 않는 빈 변수를 사용해서 원소의 수가 num인 배열을 생성한다.

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Input value what you search for: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('There is no index have value')
        # print(x)
        #print(len(x)) // this is test sentence
    else:
        print(f'Value that you are searching for is in x[{idx}].')

#배열이 맨 앞부터 순서대로 원소를 스캔하는 선형검색은 원소의 값이 정렬되지 않은 배열에서 검색할 때 사용하는 유일한 방법이다.

