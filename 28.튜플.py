#튜플
# ()
t= (10,20,30) #튜플
print(t)

t2 = 10,20,30 #튜플
print(type(t2))

t3 = 10, # or t3(10,)
print(type(t3))
print(t[0],t[1],t[2])
#t[0] = 30 #error 불변 자료형

for i in t:
    print(i)

#슬라이싱
print(t[1:])
#튜플 메서드
print ( t. count(20)) 
#index()
print(t.count(20))
t = (10,20,30)
a,b,c = t
print(a,b,c)
#값 교환
x, y = 1, 2
x, y = y, x
print(x,y)

