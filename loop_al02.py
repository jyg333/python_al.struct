# a부터 b까지 정수의 합

print('Find sum from a to b')
a = int(input('Input a:'))
b = int(input('Innput b: '))

if a > b:
    a ,b = b, a
    #파이썬에서는 이런식으로 값을 스위치 시켜주는것을 알았다.

sum = 0
for i in range(a, b): #a 부터 b-1 까지 값 뒤에 + 를 붙여 출력한다. for문의 기본적인 형식이다 0부터 n-1 까지의 범위를 반복
    print(f'{i} + ', end = '')
    sum += i

print(f'{b} = ', end = '')
sum += b

print(sum)