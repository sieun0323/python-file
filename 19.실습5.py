#while문을 사용해서
#1을 누르면 " 게임 시작"
#2를 누르면 " 게임 종료"-> while 종료됨

while True:
    a = int(input("1 or 2: "))
    if a == 1:
        print("게임 시작")
    elif a == 2:
        print("게임종료")
        break
    else:
        print("다시 입력하세요.")
     

""" while True:
    x = input("1. 게임시작, 2. 게임종료") # 재할당
    if x == "1":
        print("게임 시작")
    elif x == "2": 
        print("게임을 종료합니다.")
        break """