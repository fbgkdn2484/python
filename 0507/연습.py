def cirArea(r):
    return 3.141592 * r * r

def triArea(b, h):
    return b * h / 2

def rectArea(b, h):
    return b * h

while True:
    print("0. 끝내기")
    print("1. 원의 면적 구하기")
    print("2. 삼각형의 면적 구하기")
    print("3. 사각형의 면적 구하기")
    choice = int(input("선택해보삼 :"))
    
    if choice == 0:
        break
    elif choice == 1:
        base = int(input("밑변을 입력하시오 :"))
        height = int(input("높이를 입력하시오 :"))
        print("삼각형의 높이와 밑변은", base, height, "면적은", triArea(base, height))

