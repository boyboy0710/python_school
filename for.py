import random

random = random.randint(1,101)

for i in range(1,11):
    data = int(input("추측 값 입력:"))
    if data > random:
        print("down")
    elif data < random:
        print("up")
    else:
        print(i,"번 만에 성공")
        break

