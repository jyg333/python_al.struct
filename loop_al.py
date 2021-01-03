#반복하는 알고리즘
#1부터 n까지 정수의 합 구하기

print('Calculate sum of integer From 1 to n ')

n = int(input('Input value n.: '))

sum = 0
i =1

while i <= n:
    sum += i
    i +=1



#100 을 넣었을 때 5050 값이 나왔다.
# 가우스의 법칙이 생각 났다... (1+n)*(n/2)