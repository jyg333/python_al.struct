# seq_search() 함수를 사용하여 실수 검색하기
from searching_al import seq_search

print('Searching real Number.')
print('Caution: Input "End" when you want quit.')

number = 0
x = [] # make empty list x

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1

ky = float(input('Input value what you searching for.: '))

idx = seq_search(x, ky)

if idx == -1:
    print('There is no element that you searching for.')
else:
    print(f'Searching Value is in x[{idx}]')

# t = (4, 7, 5.6, 2, 3.14, 1)
# b = 'string'
# a = ['DTS', 'AAC', 'FLAC']
#
# print(f'{t} in index {seq_search(t, 5.6)}')
# print(f'{b} has "n" in index {seq_search(b, "n")}')
# print(f'{a} has "AAC" in index {seq_search(a, "AAC")}')

