#중첩for문
""" for dan in range(2,5):
    print(f"{dan}단")
    for num in range(1,10):
        print(f"{dan} x {num} = {dan * num}")  """

#별찍기
"""n = int(input("몇 층 찍을까요? : "))
for i in range(1, n + 1):
    print("*" * i)
    
n = int(input("몇 층 찍을까요? : "))
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

n = int(input("몇 층 찍을까요? : "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))"""
    
#첫 층을 담당,, 둘 별을 담당
""" a = int(input("몇 단 입력할까요?"))
for i in range(1,10):
    print(f"{a}x{i}={a*i}") """

# 선생님 # 1번
""" n = int(input("몇 층 찍을까요? : ")) #3
for i in range(n):  #0 1 2  
    for j in range(i+1): # 1 2 3
        print("*", end="")
    print()"""


# 2번!!!
n = int(input("몇 층 찍을까요? :")) #3
for i in range(n,0,-1):  # 321
    print(" "*(n-i), end="")
    for j in range(i): #3 2 1
        print("*",end="")
    print()

# 3번!!!
n = int(input("몇 층 찍을까요? :")) #3
for i in range(n): # 012
    print(" "*(n-i),end="")   # "*"이 1 3 5 
    print()
    for j in range(i+1):
        print("*",end="")
print()


