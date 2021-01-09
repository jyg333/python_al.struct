#선형 검색은 반복할 때마다 2가지 종료 조건을 체크한다. 그 효율을 높이기 위해서 '보초법' 을 사용해 보자
#검색하고자 하는 키값을 배열의 맨 끝에 저장한다.

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) ->int:
    a = copy.deepcopy(seq) # seq를 복사한다.
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('Input the number of element: '))
    x =[None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky  = int(input('Input the value you searchin for: '))

    idx = seq_search(x, ky)

#16 행 while 문이 종료되면 찾은 원소가 배열의 원래 데이터인지 보초인지 판단해야한다.
#i값이 len(seq)와 같으면 찾은것은 보초임으로 검색 실패 -1 을 반환

    if idx == -1:
        print('There is no element having that value.')
    else:
        print(f'Searching value is in x[{idx}].')