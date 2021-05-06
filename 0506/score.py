marks = []

for i in range(1,6):
    scr = int(input("%d 번 학생의 점수 : " % i))
    marks.append(scr)

    
print(marks)
number = 0
avg = 0
hap = 0

for mark in marks:
    number += 1
    if mark >= 60:
        print("%d 번 학생의 점수는 %d이고, 합격입니다." % (number,mark))
    else:
        print("%d 번 학생의 점수는 %d이고, 불합격입니다." % (number,mark))
    hap += mark
    
avg = hap/number

print("이 반 학생의 점수의 전체 총합은 %d 평균은 %.2f입니다." % (hap, avg))
