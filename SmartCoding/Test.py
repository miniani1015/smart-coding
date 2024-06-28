import random

random_number = random.randint(1,100)
count = 1

while True:
    my_number = int(input("1부터 100사이의 값을 입력하시오."))
    
    if my_number > random_number:
        print("다운")
        

    elif my_number < random_number:
        print("업")

    elif my_number == random_number:
        print(f"정답 {count}번만에 맞춤")
        break

    count = count + 1