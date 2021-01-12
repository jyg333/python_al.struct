#이진검색 binary search
#이진검색 알고리즘을 사용하려면 배열의 데이터가 정렬 되어 있어야 한다.
from typing import Any, Sequence

def bin_search(a : Sequence, key: Any) -> int:
    """searching element that matchs with key in sequence 'a'"""
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('Input the number of element:'))
    x = [None] * num

    print('배열의 데이터를 오름차순으로 입력하시오')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i -1]: #   바로 직전에 입력한 값보다 큰 값을 입력한다.
                break
    ky = int(input('Input the value you searching for: '))
    idx = bin_search(x, ky)

    if idx == -1:
        print('There is no element')

    else:
        print(f'The value is in x[{idx}]')


# 20 행에 return tab을 한번 더해서 오류가 발생