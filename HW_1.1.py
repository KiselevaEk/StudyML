def function_1_1(my_list, n):
    s = 0
    for i in my_list:
        if i <= n:
            s += i
    return s
import random

random.seed(42)
print(function_1_1([random.randint(0, 1000) for _ in range(10000)], 700))