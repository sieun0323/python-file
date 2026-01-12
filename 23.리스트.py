""" nums = [1,2,3,] #리스트 : 순서가 있고, 값을 바꿀 수 있다. 
num = (1,2,3) #튜플 : 순서가 있지만, 값을 바꿀 수는 없다.
person = {"name1":"김병철","name2":"홍길동"} #딕셔너리: 이름: 값(키: 값)
u = {1,2,3} #셋 : 중복을 허용하지 않는 구조
#자료구조- 리스트/튜플/딕셔너리/셋

#리스트
nums = [1,2,3]
print(nums)

print(nums[1]) #2   가장 앞자리는 0
print(nums[0]) #1 index 번호
nums[2] =25
print(nums)

nums2 = [34,23,78]
print(nums+nums2)
print(nums*3)
print(type(nums))

#구조 변경
for n in nums2:
    print(n*3)
for n in range(len(nums2)):  #3    > 0 1 2 
    print(n*4)
 """
#리스트 슬라이싱
nums = [ 10,20,30,40,50] # 0 1 2 3 4
print(nums[1:4])
print(nums[:4])
print(nums[1:])
print(nums[::2])
print(nums[::-1])

scores = [70, 78, 65, 43, 14]
r_scores = scores[-3:]
print(r_scores) #최근 점수를 받겠다.
[70, 78, 65, 43, 14] #왼쪽부터 비교...시간 복잡도와 공간 복잡도? O??? 시간이 많이 소요...과열...돈..?

#리스트 메서드 - 도구, 방법
#리스트.메서드()
nums = []
#nums = 0
nums.append(50) #리스트 추가
nums.append("시은")
nums.append([10,20])
print(nums)
#2차원 리스트 [50, '시은', [10, 20]]  
print(nums[2][1]) #20 출력
nums.insert(0, 20) #insert 원하는 위치에 값 넣기. 0번째에 20 넣기
print(nums)
nums.extend([10, 20]) 
nums.extend("시은")
nums.extend(["시은"])
print(nums)

for s in scores:
    if s >= 75:
        nums.append(s) #75이상인 수들을 nums에 추가
print(nums)

#삭제 - [20, 50, '시은', [10, 20], 10, 20, '시', '은', '시은', 78]
nums.remove(20) #지정값 삭제
print(nums)

#삭제2 - pop() 인덱스로 삭제 및 반환
last = nums.pop(2) #[10, 20] 저장 후 삭제
nums.pop(3) #삭제
print(last)
print(nums) 

#삭제3 
del nums[0]
print(nums)

#삭제4 기존 데이터 모두 삭제
""" nums.clear()
print(nums) """

#리스트 길이 확인 - len
print(len(nums)) #정수 - range(len*)
#개수(탐색) - count
print(nums.count(20))
#위치 찾기(탐색) - index
print(nums.index(10))

#순서 정렬 - sort()
nums = [30, 20, 10]
#nums.sort(reverse = False) #False 오름차순/ True 내림차순
#뒤집기 - reverse()
nums.reverse() #뒤집기
print(nums)

