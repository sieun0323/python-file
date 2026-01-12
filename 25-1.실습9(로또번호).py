#로또번호 추출기
""" import random
lotto = []
a = random.randint
lotto.append """
#중복없이
#멤버십 연산자 in / not in
""" a = 40
b = [12,40,45]
if a in b: #포함되어있다면
    print("있다.")
else:
    print("없다.")
if a not in b: #포함되어있지않다면
    print("없다.")
    append()
else:
    print("있다.") """

[1,2,3,4,5,6] #6개 출력
#1회 2회 3회 ...
#정렬 sort
#int
#결과
#1회: 1 2 3 4 5 6
#2회: 12,23,24,51,61,71
### 필수 조건(규칙)

""" 
- 1~45 중 **중복 없이 6개**
- **오름차순 정렬**
- 메뉴: `1) 추첨 2) 이력 보기 3) 종료`
- 이력은 추첨 결과를 **저장**해서 나중에 보여주기

```python
추천 로또번호 : 1 2 3 4 5 6
```

```python
추천된 이력 
1회 : 1 2 3 4 5 6
2회 : 2 3 4 5 6 7
```

1. 자동/수동 선택
    1. 자동 추첨과 입력 후 부족한 개수만 자동 채우기 """

import random
mm = [] # 이력 저장 리스트 
count=0
while True:
    x = int(input("메뉴: 1) 추첨 2) 이력 보기 3) 종료"))
    lotto = []
    if x == 1:
        while len(lotto) < 6: #len - 길이 확인
            a = random.randint(1,45) #중복 없이 어케함? 
            if a not in lotto: #lotto에 포함되지 않은 수 
                lotto.append(a) #a를 lottto
        lotto.sort(reverse = False) 
        count += 1 
        for i in lotto: #lotto 안에 수가 i가 되어서...하나씩 돌아감...
            print(i,end=" ") #i출력 연속으로...
        print() 
        mm.append([count,lotto]) 
    elif x == 2: 
        for l in range(len(mm)): # 0 - count 1 - lotto // mm에 있는 l들이 돌아감(?)
            print(f"{mm[l][0]}회:",end=" ") 
            for i in mm[l][1]: 
                print(i,end=" ")
            print()
    else:
        break