#구구단
#for문 연산을 위해 작성하고...
#input을 통해서 몇 단 입력할까요? #10.입력문
#출력
#2 x 1 = 2 ... 2 x 9 = 18

b = int(input("몇 단 입력할까요?"))
for i in range(1,10):
    print( b , "x" , i , "=" , b*i )
 
#print (f"제 이름은 {name}입니다. 제 나이는 {age}살입니다.")

a = int(input("몇 단 입력할까요?"))
for i in range(1,10):
    print(f"{a}x{i}={a*i}") 
#문자열 포맷팅
#유경언니 도움 엇이 처음 완성!!!!