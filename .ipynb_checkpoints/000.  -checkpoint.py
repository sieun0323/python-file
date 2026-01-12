# if -> try

import random       # 내장 라이브러리 설정

rank = []           
rank_1 = []         # 난이도별 랭킹 리스트 정의 
rank_2 = []         # 게임 후 이름과 시도횟수가 들어감
rank_3 = []


def getrank(level):     #난이도를 받는 함수(getrank) 정의 / 매개변수는 level로 설정
    if level == 1:      #난이도 별 사용자 기록을 저장하는 리스트 설정
        rank = rank_1
    elif level == 2:
        rank = rank_2
    elif level == 3:
        rank = rank_3
    return rank 

def game(level):        # 업앤다운 게임을 돌리는 사용자 정의 함수 / 매개변수는 level로 설정
    if level == 1:      # 난이도가 1 일때,
        max_num = 50    # 제일 큰 수는 50으로 설정
        rank = rank_1   # 랭킹이 들어갈 리스트 설정
        hint = False    # 힌트모드 X
    elif level == 2:
        max_num = 250
        rank = rank_2
        hint = False
    elif level == 3:
        max_num = 500
        rank = rank_3
        hint = True     # 힌트모드 O
    else:               # 1,2,3을 제외한 다른 값을 입력시, 난이도 선택이 다시 표시
        print("난이도 선택이 올바르지 않습니다.") 
        return

    while True:  #업앤다운 게임 'while'문
        answer = random.randint(1, max_num) #max-num까지 난수 설정
        count = 0 #게임시작시에는 시도횟수 0 으로 설정

        while True:  # 정답 입력에 대한  'while'문
            try:
                x = int(input("숫자를 입력하세요: "))
            except:                                 #int는 정수값을 받기 때문에 다른 값을 받으면 오류 발생
                print("숫자입력하세요!!!!!!!!!!!!")   # 경고문 
            count += 1                              # 시도횟수 한번씩 추가됨

            if hint and count == 3:                 # 3회 이상 시도했다면 힌트모드 선택 가능
                hint = int(input("힌트를 보시겠습니까?(십의 자리 반환) 1.yes 2.no: "))
                if hint == 1:                       
                    print((answer % 100) // 10)     # 힌트모드 선택하면 십의 자리 반환

            if answer > x:
                print("up")                         # 입력한 값이 정답보다 작다면 up
            elif answer < x:
                print("down")                       # 입력한 값이 정답보다 크다면 down 
            else:
                print(f"정답입니다. {x}이고 시도횟수는 {count}입니다.")
                name = input("이름을 입력하세요: ").strip()  
                rank.append([count, name]) #시도횟수와 이름이 랭킹 리스트에 저장
                break  
        retry = int(input("다시 하시겠습니까?(1.yes 2.no): "))
        if retry != 1: # != >>>>1이 아니라면 업앤다운 while문 종료
            break

def system():                                       #관리자 모드 선택 시 아이디와 패스워드 입력
    id = input("id :  ")
    pw = input("pw :  ")
    if id == "sieun0323" and pw == "0323":          #아이디와 패스워드가 일치한다면
        getrank(level)                              #관리자 모드 설정 가능
        s = int(input("1. 랭킹 초기화  2) 없음 "))
        if s == 1:                                  #랭킹 초기화 선택시
            rank.clear()                            #해당난이도의 랭킹 초기화
            print(rank)                             #초기화 확인용
            print("해당 난이도의 랭크가 초기화되었습니다. ")
    else:
        print("id나 pw가 틀렸습니다. 메뉴 화면으로 돌아갑니다. ")
    


def ranking(level):                                         #랭킹 확인 사용자 정의 함수 설정
    rank = getrank(level)                                   #getrank 함수를 rank 로 설정
    rank.sort()                                             #랭킹 정렬
    for i in range(min(5,len(rank))):                       #5위까지 출력
        print(f"{i+1}위 {rank[i][1]} {rank[i][0]}회")


# 게임코드
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
        level = int(input("난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 :"))
        system()
        
    if menu == 5:
        print("게임이 종료되었습니다.")
        break