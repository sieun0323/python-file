#셋 set
#생성/출력(중복 제거 + 순서 없음)
s = { 10, 20 ,20,30}
print(s)
s. add(40) 
#여러 값 추가 - update()
s. update([10,20,30,50])

#값 삭제 - remove
#s.remove(99) 
s.remove(30)

print(s) 
#값 삭제 2 - discard()
s.discard(99) # 없으면 무시
# 값 삭제 3 - pop()임의의 값 삭제 후 반환
x = s.pop()
print (x)
print(s)
names = ["민수" , "철수", "민수", "영희"]
uniqe = set(names)
print (uniqe)

#전체 삭제 clear()
s.clear()
print(s)

print ( 20 in s) 

#집합 연산 
a= {1,2,3}
b = {3,4,5}
print (a | b) #합집합       or
print (a & b) #교집합       and
print (a - b) #차집합       not
print (a ^ b) #대칭차집합    xor

#비트 연산자와 논리 연산자
print("" or "mes")              # 앞이 비어있으면 뒤를 선택
print (" mes " or "message")    # 앞이 있으면 앞을 선택
print (0 and 999)               # 앞이 False면 앞을 반환
print (10 and 999)              # 앞이 True면 뒤를 반환

#좌석 배치 변경 전/후
before = {("A",1),("A",2),("B",1)}
after = {("A",1),("B",1),("B",2)}
print("공통좌석: ",before & after)
print("사라지 ㄴ좌석:",before -after)
print("추가된 좌석",after - before )
print("변경된",before ^after)