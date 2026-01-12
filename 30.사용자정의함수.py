# 사용자 정의 함수 def
print ("학생 목록 출력")
print(" eee - 99")
print(" fff - 80")
def show_students():
    print("학생 목록 출력")
    print("kim - 90점")
    print("lee - 80")
show_students()
show_students()
# 조건
# 2번 이상 반복될 때
# while/if 구조 자체의 반복
# 한 함수가 입력/처리/출력 -> 나누기
# 한 번 고치면 여러 곳을 고쳐야 할 때 

""" def 함수이름(매개 변수 a, b): 
    실행할 코드 

함수이름(매개변수) """

def add(a, b):      # a b 는 매개변수: 값을 밖에서 갖고오는 변수임
    return a + b    # 연산을 하고 , 가지고 있는다  -> 반환 
print(add(3, 4))    # 인자 (인수)

def add(a, b="안녕하세요"):      
    print(b, a)  

#가변인자
def total(*args):
    print(args)     #args = 인자 
total ( 1,2,3,4)    #튜플 - 변하지 않는 

def sum_all(*nums):
    total = 0 
    for n in nums : 
        total += n 
    return total
print(sum_all(1,2,3,4,5))

#가변 딕셔너리
def show_info ( **kwargs):
    print(kwargs)
show_info()

def show_info ( **info):
    for k, v in info.items():
            print(k, ":", v)
show_info(name = "kim", score =[80,90] ,scores = 80, grade = "c" )

def example (a, *args, **kwargs): 
    print(a)
    print(args)
    print(kwargs)
example(1,2,3,4,name= " sieun")

#업앤다운 - 로또 - 가위바위보
#업앤다운만 def game()
#game()
#if a = "1"             # 1을 눌렀을 때 게임이 실행되도록 
    # 게임 -> game()
# 뼈대 - 핵심 기능 - 테스트 - 리팩토링
# EX) 뼈대 : 1번 게임 시작 / 2번 게임 종료
# 핵심 기능 : 게임을 만든다
# 테스트 문제 찾기 
# 리팩토링 (결과는 같은데 구조나 함수를 묶는)
# 메뉴
# 입력 - 게임 - 출력
# 출력 - 정답입니다. 뭐시기뭐시기
# 테스트 - 문자/숫자 예외 처리 고민
# 리팩토링 
# main.py
# print. py
# ...

""" def game1()
def game2()
def game4(a, b)
    v = a + 1
    n = b + 1
    return v, n
    if a == 1:
        return a
    elif b == 2:
        return b
 """



#하드웨어#소프트웨어만 def로 묶으라고? 
"""1. 게임시작
    game1() - 업앤 다운
    -> game2() - 로또번호   #소프트웨어 - 로또번호
2. 게임종료"""

# 전역변수 / 지역변수
import random
# def # 먼저 선언해주기
# while if for def 등등 밖에 있으면 전역변수 안에 있으면 지역변수 
# 실행이 안되면 전역변수인지 확인

x = 10 #전역
def func(): 
    y = 5
    print (y)
    print(x)
    return (y)
#print (x,y) #줄 그어져 있다면 정의가 안된 것


""" x =10
def func1():
    x = x + 1
    return x
func1() """
# immutable(변경불가) vs mutable(변경가능)
# immutable(변경불가)
# 숫자, 문자, 튜플
# mutable
# 리스트, 딕셔너리, 셋

#실행 가능
x =10
def func1(): #연산만 할 수 있도록
    return x +1
func1()

data1 = {"x": 10 }
def func3(s):
    s["x"] += 1

func3(data1)
print (data1) #원본 수정 상태로 출력됨

#원본 유지!
data2 = {"x": 10 }
def func4(s):
    data3 = s.copy()
    data3["x"] +=1
    return data3
new_data = func4(data2)

print(data2) # 원본
print ( new_data) # 수정본

#과제 
# 1. 업앤다운 게임 def 묶어서 전체 코드 업로드
# 2. 업앤다운 게임 def main(), ask(), input(), 입력/ 출력/ 게임/ 메뉴 

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
                name = input("이름을 입력하세요: ")
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
        level = int(input(" 난이도 선택 1.쉬움 1-50 2.보통 1-100 3.어려움 1-500 : "))
        system(level)
        
    if menu == 5:
        print("게임이 종료되었습니다.")
        break