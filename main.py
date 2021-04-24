name = input("이름입력=")
a = int(input("점수입력="))

if a >= 90:
    hakjum = "A"

elif a>= 80:
    hakjum = "B"

elif a>= 70:
    hakjum = "C"

elif a>= 60:
    hakjum = "D"

else:
    hakjum = "F"

print(name,"님의 학점은",hakjum,"입니다")