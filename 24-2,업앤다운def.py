# if -> try

def game(level): 
    if level == 1:
        max_num = 50
        rank = rank_1
        hint = False
    elif level == 2:
        max_num = 100
        rank = rank_2
        hint = False
    elif level == 3:
        max_num = 500
        rank = rank_3
        hint = True
    else:
        print("난이도 선택이 올바르지 않습니다.")
        return

    while True:  
        answer = random.randint(1, max_num)
        count = 0

        while True:  # 업다운 한 판
            x = int(input("숫자를 입력하세요: "))
            count += 1

            if hint and count == 3:
                hint = int(input("힌트를 보시겠습니까?(십의 자리 반환) 1.yes 2.no: "))
                if hint == 1:
                    print((answer % 100) // 10)

            if answer > x:
                print("up")
            elif answer < x:
                print("down")
            else:
                print(f"정답입니다. {x}이고 시도횟수는 {count}입니다.")
                name = input("이름을 입력하세요: ").strip()   #여기
                rank.append([count, name])
                break  # 한 판 종료

        retry = int(input("다시 하시겠습니까?(1.yes 2.no): "))
        if retry != 1:
            break
def system(level):
    if level == 1:
        rank = rank_1
    elif level == 2:
        rank = rank_2
    elif level == 3:
        rank = rank_3
    
    s = int(input("1. 랭킹 초기화  2) 없음 "))
    if s == 1:
        level = int(input("난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 :"))
        rank.clear()
        print(rank)
        print("해당 난이도의 랭크가 초기화되었습니다. ")
def ranking(level):
    if level == 1:
        rank = rank_1
    elif level == 2:
        rank = rank_2
    elif level == 3:
        rank = rank_3
    rank.sort()

    for i in range(min(2,len(rank))):
        print(f"{i+1}위 {rank[i][1]} {rank[i][0]}회")

import random
rank_1 = []
rank_2 = []
rank_3 = []

while True:
    menu = int(input("1) 게임 시작  2) 랭킹 보기  3) 도움말 4) 관리자 모드 5) 게임 종료 : "))
    if menu == 1:
        level = int(input(" 난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        game(level)

    if menu == 2:
        level = int(input("난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        ranking(level)
        
    if menu == 3:
        print("[설명서] \n게임방법")
        print("""1. 게임 시작 후 난이도를 설정하세요.
2. 숫자를 입력하여 정답을 맞춰보세요.
3. 정답을 맞춘 후 이름을 입력하고 랭킹을 확인해보세요 !4. 랭킹은 5위까지 나타납니다.
5. 게임을 종료하려면 메뉴에서 5를 누르세요.
6. 관리자 모드에서 랭킹을 초기화할 수 있습니다.""")
    if menu == 4: # 랭킹 초기화/ 임의 기능 추가
        #level = int(input(" 난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        system(level)
        
    if menu == 5:
        print("게임이 종료되었습니다.")
        break
