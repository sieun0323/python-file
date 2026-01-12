import random
listt = []
count=0
def popo():
    global count
    while len(lotto) < 6: #len - 길이 확인
        a = random.randint(1,45) #중복 없이 어케함? 
        if a not in lotto: #lotto에 포함되지 않은 수 
            lotto.append(a) #a를 lottto 여기까진 ㅇㅋ
    lotto.sort(reverse = False) #로또 정렬
    count += 1 #count 1회 추가
    for i in lotto: #lotto 안에 수가 i가 되어서...하나씩 돌아감...즉 i 가 a인셈
        print(i,end=" ") #i출력 연속으로...
    print() 
    listt.append([count,lotto]) 

listt = [] # 이력 저장 리스트 

while True:
    x = int(input("메뉴: 1) 추첨 2) 이력 보기 3) 종료"))
    lotto = []
    if x == 1:
       popo()
    elif x == 2: 
        for l in range(len(listt)): # 0 - count 1 - lotto // listt에 있는 l들이 돌아감(?)
            print(f"{listt[l][0]}회:",end=" ") 
            for i in listt[l][1]: 
                print(i,end=" ")
            print()
    else:
        break