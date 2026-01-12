import random
rank_1 = []
rank_2 = []
rank_3 = []
#random.seed(1) #난수 고정
# 랭킹을 사용자 정의 함수로 
# game()
# if a = '1"
    # 게임 => game() 

while True:
    menu = int(input("1) 게임 시작  2) 랭킹 보기  3) 도움말 4) 관리자 모드 5) 게임 종료 : "))
    if menu == 1:
        level = int(input(" 난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        if level == 1:
            count = 0
            a = random.randint(1,50)
            while True:
                x = int(input("숫자를 입력하세요: "))
                count += 1
                if a > x:
                    print("up")
                elif a < x:
                    print("down")
                elif a == x:
                    print(f"정답입니다.{x}이고 시도횟수는 {count}입니다.")
                    name = input("이름을 입력하세요: ")
                    rank_1.append([count,name])
                    retry = int(input("다시 하시겠습니까?(1.yes 2.no)"))
                    if retry == 1:
                        count = 0
                        a = random.randint(1,3)
                        continue # ← 여기서는 a를 새로 만들지 않음/ 바로 위 while문으로 돌아가니께...
                    else:
                        break
                    
                    
        if level == 2:
                count = 0
                b = random.randint(1,100)
                while True:
                    x = int(input("숫자를 입력하세요: "))
                    count += 1
                    if b > x:
                        print("up")
                    elif b < x:
                        print("down")
                    elif b == x:
                        print(f"정답입니다.{x}이고 시도횟수는 {count}입니다.")
                        name = input("이름을 입력하세요: ")
                        rank_2.append([count,name])
                        retry = int(input("다시 하시겠습니까?(1.yes 2.no)"))
                        if retry == 1:
                            count = 0
                            b = random.randint(1,100)
                            continue
                        else:
                            break
        if level == 3:
            count = 0
            c = random.randint(1,500)
            while True:
                x = int(input("숫자를 입력하세요: "))
                count += 1
                if count == 3:
                    hint = int(input("힌트를 보시겠습니까?(십의 자리 반환) 1.yes 2.no"))
                    if hint == 1:
                        print((c-(c//100*100))//10)
                if c > x:
                    print("up")
                elif c < x:
                    print("down")
                elif c == x:
                    print(f"정답입니다.{x}이고 시도횟수는 {count}입니다.")
                    name = input("이름을 입력하세요: ")
                    rank_3.append([count, name])
                    retry = int(input("다시 하시겠습니까?(1.yes 2.no)"))
                    if retry == 1:
                        count = 0
                        c = random.randint(1,500)
                        continue
                    else:
                        break
    if menu == 2:
        rank_1.sort() #sort는 정렬
        rank_2.sort()
        rank_3.sort()
        level = int(input("난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        if level == 1:
            for i in range(0,5): # 0 1 2 3 4 :5개 
                print(f"{i+1}위 {rank_1[i][1]} {rank_1[i][0]}회")
        if level == 2:
            for l in range(0,5):
                print(f"{l+1}위 {rank_2[l][1]} {rank_2[l][0]}회")
        if level == 3:
            for w in range(0,5):
                print(f"{w+1}위 {rank_3[w][1]} {rank_3[w][0]}회")
    if menu == 3:
        print("[설명서] \n게임방법")
        print("""1. 게임 시작 후 난이도를 설정하세요.
2. 숫자를 입력하여 정답을 맞춰보세요.
3. 정답을 맞춘 후 이름을 입력하고 랭킹을 확인해보세요 !4. 랭킹은 5위까지 나타납니다.
5. 게임을 종료하려면 메뉴에서 5를 누르세요.
6. 관리자 모드에서 랭킹을 초기화할 수 있습니다.""")
    if menu == 4: # 랭킹 초기화/ 임의 기능 추가
        s = int(input("1) 랭킹 초기화  2) "))
        if s == 1:
            level = int(input("난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 :"))
            if level == 1:
                rank_1.clear()
                #print(rank_1)
                print("난이도1의 랭크가 초기화되었습니다.")
            if level == 2:
                rank_2.clear()
                #print(rank_2)
                print("난이도2의 랭크가 초기화되었습니다.")
            if level == 2:
                rank_3.clear()
                #print(rank_3)
                print("난이도3의 랭크가 초기화되었습니다.")
    if menu == 5:
        print("게임이 종료되었습니다.")
        break

    # 임의 기능...? 랭킹조작...? 

    #궁금한 점
    # 줄바꿈하려면 print를 따로 쓰는 방법밖에 없나요? 
    # 게임을 5번까지 안해도 랭킹을 나타내고 싶어요. 