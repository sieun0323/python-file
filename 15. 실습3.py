# 조건문
id = input("id 입력 :  ")
password = input("pw 입력 :  ")
if id == "sieun0323" and password == "1234":
    print ("로그인이 완료되었습니다.")
else:
    print("로그인이나 비밀번호가 틀렸습니다.")

#다중, 중첩 조건문
# 로그인을 하고, 사용한 금액이 어느정도인가요?input
""" 1천만원
5천만원
1억 
어떤 등급이고 혜택은 어떤 게 있다. """

""" id = input()
password = input() """
사용금액 = int(input("사용 금액 :  "))

""" if password == "1234":
    print("로그인이 완료되었습니다.")
else:
    print("아이디나 비밀번호가 틀렸습니다.") """

if 사용금액 >= 100000000:
    print("A등급입니다")
elif 사용금액 >= 50000000:
    print("B등급입니다.")
else:
    print("c등급입니다.")

#여러분의 지갑에 얼마 있나요? 

t=int(input("가진 재산을 말하면 점심을 추천하겠다. \n 나의 전재산:  "))
if t >= 26000:
    print("치킨먹어라")
elif t >=14000:
    print("떡볶이 먹어라")
else: 
    print("굶어라")