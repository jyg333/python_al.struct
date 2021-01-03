# 변수가 하나만 있을 떄는 while문 보다 for문이 좋다.
#1부터 n 까지의 정수의 합 구하기

print('Sum from 1 to n')
n = int(input('Input integer n: '))

sum = 0
i =1
for i in range(1, n+1):

    sum = sum + i
    #That is same (sum  += i)


print(f'Sum of integer from 1 to {n} is {sum}.')