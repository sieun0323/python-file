import random
listt = []
count=0
def popo():
    global count
    while len(lotto) < 6:
        a = random.randint(1,45) 
        if a not in lotto: 
            lotto.append(a) 
    lotto.sort(reverse = False) 
    count += 1 
    for i in lotto:
        print(i,end=" ") 
    print() 
    listt.append([count,lotto]) 

listt = [] 

while True:
    x = int(input("메뉴: 1) 추첨 2) 이력 보기 3) 종료"))
    lotto = []
    if x == 1:
       popo()
    elif x == 2: 
        for l in range(len(listt)): 
            print(f"{listt[l][0]}회:",end=" ") 
            for i in listt[l][1]: 
                print(i,end=" ")
            print()
    else:
        break