'''
hap = 0 
i = 1
while i <= 100:
    hap = hap + i
    i += 1

print("합 = %d" % hap)

oddhap = 0
evenhap = 0
hap = 0
i = 1
while i <= 100:
    hap = hap + i
    if i % 2 == 0:
        evenhap = evenhap + i
    else:
        oddhap = oddhap + i
    i += 1

print("총합 = %d" % hap)
print("짝수 합 = %d" % evenhap)
print("홀수 합 = %d" % oddhap)


sevenhap = 0
i = 1
while i <= 100:
    if i % 7 == 0:
        sevenhap += i
    i += 1

print("1부터 100까지의 7의 배수 합 = %d" % sevenhap)



hap = 0
i = 1
while i <= 100:
    hap = hap + i
    if hap >= 1000:
        break
    i += 1

print("1부터 100까지의 합 중에 처음으로 1000을 넘는 수 %d와  합  = %d" % (i ,hap))
'''


hap = 0
i = 0
while i <= 100:
    i += 1
    if i % 7 == 0:
        continue
    hap += i
  
print("1부터 100가지의 합중에 7의 배수를 생략한 합 = %d" % hap)
        
