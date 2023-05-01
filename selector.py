import random

result = random.sample(range(1, 46), k = 6)


lot_List = []
final_list = []

i = int(input("반복횟수 입력: "))

for i in range(i):
    for j in range(6):
        num = random.randrange(1, 46)
        lot_List.append(num)
    

print(lot_List)