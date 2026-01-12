# 문법 -> 사고(알고리즘)
# 기획력(?)
# 전역 변수 / 지역 변수 

"""c = 0 #전역
while True:
    c = 0 # 지역
    while:
    for:
    if:"""


#사용자가 입력을 하면 입력한 값과 랜덤을 나온 값과 비교
#승/패 만들기
#1.게임시작
#1)3판 선승제
#2)단일게임
#2.게임종료

import random
c = ["가위","바위","보"]
w = "승리"
l = "패배"
count_w=0 
count_l=0
#t = "무승부"
while True:
    menu = int(input("1.게임시작 2.게임종료 : ")) # 와일문
    while True: 
        if menu ==1:
            menu_2 = int(input("1.3판 선승제  2.단일제"))
            if menu_2 == 1:
                print("3판 선승제를 선택하셨습니다.n/게임은 총 3번 진행됩니다.")
                while True: #와일문#이프 승리조건 하나로 묶고. 패배도. 무승부
                    x= input("가위 바위 보 중 하나를 입력하세요.\n나:")
                    a = random.choice(c)
                    print(f"상대방: {a}")
                    if (x == "가위" and a == "보") or (x == "바위" and a =="가위") or (x == "보" and a =="바위"): 
                        print(f"{w}하셨습니다.")
                        count_w+=1 
                    elif (x == "가위" and a == "바위") or (x == "바위" and a =="보") or (x == "보" and a =="가위"): 
                        print(f"{l}하셨습니다.")
                        count_l += 1
                    elif x==a:
                        print("무승부입니다.")
                        # 2 이상일때 중단
                    
                    if (count_w >= 2) or (count_l >=2):
                        if count_w >= 2:
                            print("완승!!!!!")
                            count = 0
                            break
                        elif count_l >= 2:
                            print("완패!!!!!")
                            count = 0
                            break
                break
            
            elif menu_2 == 2:  
                print("단일제를 선택하셨습니다. 게임은 한 번만 진행됩니다.")  
                while True:   
                    x= input("가위 바위 보 중 하나를 입력하세요.")
                    a = random.choice(c)
                    print(f"상대방: {a}")
                    if (x == "가위" and a == "보") or (x == "바위" and a =="가위") or (x == "보" and a =="바위"): 
                        print(f"{w}하셨습니다.")
                        count_w+=1 
                        break
                    elif (x == "가위" and a == "바위") or (x == "바위" and a =="보") or (x == "보" and a =="가위"): 
                        print(f"{l}하셨습니다.")
                        count_l += 1
                        break
                    elif x==a:
                        print("무승부입니다.")
                    break
                break
                    

                
        elif menu == 2:
            print("게임이 종료되었습니다.")  
            break 
            