#세 정수를 입력받아 중앙값 구하기

def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c: # a가 b보다 작은 경우 중에서 c보다는 큰경우
        return a
    elif a < c:
        if c > b:
            return b
        elif c < b:
            return c
        else:
            return b
print('Find middle value of  three integers.')
a = int(input('value of integer a :'))
b = int(input('value of integer b :'))
c = int(input('value of integer c :'))

print(f'The Middle value is {med3(a, b, c)}.')
#f string을 활용 했다. 아직 잘 f string 에는 여러가지 방법이 있지만 이 방법을 선호한다.
#세개의 정수가 서로 같은 값일 경우는 고려하지 않았다.
