#외장/ 내장 라이브러리
import random # 내장 라이브러리
#random이라고 하는 import 라이브러리? 
a = random.randint(1,100) #1부터 100까지 정수값 반환
#업앤다운
# 56        input=40        56>40 "더 높게 입력해주세요!"

#1. 값을 맞추면 "정답입니다! {}이였고, 시도횟수는 {}번이었습니다."
#2. 게임이 끝나면 메뉴로
#3. 2번을 누르면 게임종료

a = random.randint(1,100)
while True:
    x=int(input("1. 게임시작, 2. 게임종료 :"))
    if x == 1:
        count = 0
        while True:
            # 여기 한번마 하면된다고?
            s= int(input("숫자를 입력해주세요."))
            if s>a:
                print("다운")
                count+=1
            elif s<a:
                print("업")
                count+=1
            elif s == a:
                print(f"정답입니다! {s}였고, 시도횟수는 {count}번 입니다.")
                break
    elif x == 2:
        break


"""     if x == 1:
        print("게임시작")
        while true:
            count+=1 
            s = int(input("값을 입력해주세요"))
            if s == a:
                print(f"정답입니다! {s}이였고, 시도횟수는 {count}번 입니다!")
    elif x == 2
        break """