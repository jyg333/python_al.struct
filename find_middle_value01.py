def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a > b and c > b):
        return b
    else:
        return c
print('Find middle value of  three integers.')
a = int(input('value of integer a :'))
b = int(input('value of integer b :'))
c = int(input('value of integer c :'))

print(f'The Middle value is {med3(a, b, c)}.')

#if 문에서 조건식이 성립하지 않으면 elif문을 수행 할 필요가 없음 으로 비효율적이다.
#아직은 이런 부분의 효율성에 대한 이해가 부족한듯 하다.