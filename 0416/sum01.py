'''
print("유하우")
print("202106042")
print("유하우", end=" ")
print("202106042")
'''

'''i 는 변수이름'''

num = int(input("정수 입력 : "))
sum = 0
for i in range(1, num+1):
    if i < num:
        print(i, "+", end= " ")
    else:
        print(i, "=", end= "")
    sum += i
print(sum)


