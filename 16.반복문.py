#반복문
"""for 변수 in 반복횟수/범위: 
    명령블록1
    명령블록2
    명령블록3
#숫자를 반환 받는 for문
for i in range(5): # 숫자만 쓰면 걍 0 부터 시작함
    print(i)
#문자 자체를 반복하는 for문 
for i in range(5): # 숫자만 쓰면 걍 0 부터 시작함
    print("안녕")

for i in range(5): # 숫자만 쓰면 걍 0 부터 시작함
    print(f"{i+1}위 입니다.")

for i in range(1,6): # 숫자만 쓰면 걍 0 부터 시작함,,
    print(f"{i}위 입니다.")"""

#300400500이 출력되도록 
"""for i in range(3,6):
    print(i*100, end="")

for i in range(1,6,2):
    print(i)"""
#3의 배수, step 사용, if 사용 100까지만

"""for i in range(3,100,3):
    print(i)"""

for i in range(3,100):
    if i%3 == 0:
       print(i)

"""*
**
***
****
*****
#for문 무조건 1개만 /input("몇 층 찍으실건가요?")
*****
 ****
  ***
   **
    *

    *
   ***
  *****
 *******
*********"""

print("몇 층?")
r= int(input())
for i in range(r+1):
    print("*"*i)

print("몇 층?")
for i in range(r,0,-1):
    print(" "*(r-i),i*"*")

print("몇 층?")
r= int(input())
for i in range(r+1):
    print(" "*(r-i), "*"*(2*i-1), )