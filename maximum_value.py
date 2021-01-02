#세 정수의 최대값 구하기

def max3(a, b, c):
    maximum = a
    if b > maximum: maximum = b
    if c > maximum: maximum = c
    return maximum

print(f'max3(3, 2, 1) = {max3(3, 2, 1)}')
print(f'max3(4, 5, 7) = {max3(4, 5, 7)}')
print(f'max(100, 999, -89) = {max3(100 ,999, -89)}')