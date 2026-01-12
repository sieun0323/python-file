import random
import os

filename = "ranking.txt"

# 1) 파일 없으면 생성
if not os.path.exists(filename):
    f = open(filename, "w", encoding="utf-8")
    f.close()

# 2) 파일에서 랭킹 불러오기 -> [[tries, name], [tries, name], ...]
ranking = []

f = open(filename, "r", encoding="utf-8")
lines = f.readlines()
f.close()

for line in lines:
    line = line.strip()  # 줄 끝 개행 제거
    if line == "":
        continue

    parts = line.split(",")   # ["3", "철수"]
    if len(parts) != 2:
        continue

    tries_str = parts[0].strip()
    name = parts[1].strip()

    # tries가 숫자인지 간단히 확인
    if tries_str.isdigit():
        tries = int(tries_str)
        ranking.append([tries, name])

# 3) 기존 TOP5 출력
ranking.sort()  # tries(시도횟수) 기준 오름차순 정렬 (리스트 첫 값 기준)
print("\n===== 기존 랭킹 TOP 5 =====")
if len(ranking) == 0:
    print("아직 랭킹 기록이 없습니다.")
else:
    top = ranking[:5]
    for i in range(len(top)):
        print(f"{i+1}위) {top[i][1]} - {top[i][0]}회")
print("==========================\n")


# -------------------
# 4) 업앤다운 게임 시작
# -------------------
answer = random.randint(1, 2)
tries = 0

print("업앤다운 게임 시작! (1~100)")
while True:
    guess = input("숫자 입력: ")

    if guess.isdigit() == False:
        print("숫자만 입력해 주세요.")
        continue

    guess = int(guess)
    tries += 1

    if guess < answer:
        print("UP")
    elif guess > answer:
        print("DOWN")
    else:
        print(f"정답! {tries}번 만에 맞췄습니다.")
        break

# 5) 닉네임 입력 받고 랭킹에 추가
name = input("닉네임을 입력하세요: ").strip()
if name == "":
    name = "익명"

ranking.append([tries, name])

# 6) txt 파일에도 즉시 저장(한 줄 추가)
f = open(filename, "a", encoding="utf-8")
f.write(f"{tries},{name}\n")        # 이스케이프 문자/ 함수 
f.close()                           #strip()은 줄바꿈도 제거!

# 7) 정렬 후 TOP5 출력
ranking.sort()

print("\n===== 최신 랭킹 TOP 5 =====")
top = ranking[:5]
for i in range(len(top)):
    print(f"{i+1}위) {top[i][1]} - {top[i][0]}회")
print("==========================")