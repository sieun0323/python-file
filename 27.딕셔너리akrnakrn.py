#리스트 1차원 2차원
#딕셔너리
person = {"name1": "홍길동", "age":22, "s": [1,2,3,]}# 이름:값 키:값
print(person)
print(person["name1"])
print(person["s"])
student = {"name":"홍길동", "age":20, "grade":3}
print("이름:",student["name"])

person["name1"]="김병철"
person["이름"] = "김병철"
person["age"] = 21
#같은 경우 변경 없는 경우 추가
print(person)

for K in person:
    print(K)#key
    print(person[K])#value
    #여러학생의정보관리
students=[
    {"name":"민수","score":80},
    {"name":"성민","score":60},
    {"name":"은혁","score":70}
]

for s in students: #리스트 반복문
    print(s["name"],s["score"])
total = 0
for s in students: #리스트 반복문
    total +=s["score"]
print("평균점수:", total/len(students))
student = {"name": "홍길동","age":20,"grade":3}

#딕셔너리 메서드
print(person. get("age"))
print (person .get(" name"))
# 값 갱신 추가
print (person.update({"age":22,"city":"seoul"}))
print(person)
#값 삭제1
a = person.pop("s")
print(a)
print(person)
del person["이름"]
print(person)

#마지막 요소 삭제 - popitem()
k,v = person. popitem()
print(k,v)
print(person)
#전체 삭제 칟ㅁㄱ()
person. clear()
print(person)
print(len(person)) #정수로 반환

#키 기준  포함여부 in 
print("name1" in person)
print("age" in person)