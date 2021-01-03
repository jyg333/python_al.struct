#pass 명령어 사용해 보기

n = int(input('Input a integer: '))

if (n >= 0 and n < 10):
    print("일의 자리 수 입니다")
elif (n >= 10 and n < 100):
    print("십의자리 숫자 입니다.")
else:
    pass
#100 이상의 정수를 입력 했을때는 Process finished with exit code 0 로 끝이 났다.
