# 학생 5명의 시험 점수를 입력받아 합계와 평균을 출력!!

print('Count Group of Student mutipulation and average')

score1 = int(input("""First Student's point: """))
score2 = int(input("""Second Student's point: """))
score3 = int(input("""Third Student's point: """))
score4 = int(input("""Fourth Student's point: """))
score5 = int(input("""Fifth Student's point: """))

total =0
total += score1
total += score2
total += score3
total += score4
total += score5

print(f'Total is {total} point.')
print(f'Average is {total / 5} point.')