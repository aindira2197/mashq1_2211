import random

#1-misol
print(random.randint(1, 100))

#2-misol
print(random.random()) 

#3-misol
lst = [10, 20, 30, 40, 50]
print(random.choice(lst))

#4-misol
juft_son = random.choice([i for i in range(1, 51) if i % 2 == 0])
print(juft_son)

#5-misol
nums = [random.randint(1, 100) for _ in range(5)]
print(nums)

#6-misol
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

#7-misol
print(random.sample(range(1, 11), 3))

#8-misol
print(random.choice(["yutdingiz", "yutqazdingiz"]))

#9-misol

nums = [i for i in range(100, 201) if i % 5 == 0]
print(random.choice(nums))

#10-misol
print(random.choice(["qizil", "yashil", "ko'k"]))


