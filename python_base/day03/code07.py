import random

score = 0
for i in range(5):
    random_mun01 = random.randint(1, 10)
    random_mun02 = random.randint(1, 10)

    result_input = int(input("calculate:"+str(random_mun01)+"+"+str(random_mun02)+"=?"))

    if result_input == random_mun01 + random_mun02:
        score += 10
    else:
        score -= 5
print(score)


