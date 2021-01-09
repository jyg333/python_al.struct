from searching_al01 import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
b = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'{t} in index {seq_search(t, 5.6)}')
print(f'{b} has "n" in index {seq_search(b, "n")}')
print(f'{a} has "AAC" in index {seq_search(a, "AAC")}')
#문자열도 시퀀스 이다.
