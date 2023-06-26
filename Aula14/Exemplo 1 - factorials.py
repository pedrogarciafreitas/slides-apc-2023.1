def factorial(n):
    fact = 1
    if n > 1:
        fact = factorial(n-1) * n
    return fact


def factorial_error(n):
    return factorial_error(n-1) * n


for i in range(10):
    # print(i,factorial(i))
    print(i, factorial_error(i))