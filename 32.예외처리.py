try:
    x =int(input("숫자 입력: "))
    result = 10 / x
except ValueError:
	print("숫자를 입력해야 합니다.")
except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.") 
	
def attempt_float(x):
    try:
        return float(x)
    except ValueError:
        return "잘못된 입력입니다"
    
a = input("숫자을 입력하세요 :")
print(attempt_float(a))

try:
  age =int(input("나이 입력: "))
except ValueError:
	print("숫자를 입력하세요.")
#성공했을 때만
else:
	print("입력 성공:", age)

try:
    age =int(input("나이 입력: "))
except ValueError:
		print("오류 발생")
#항상 실행되는 블록
finally:
		print("프로그램 종료")