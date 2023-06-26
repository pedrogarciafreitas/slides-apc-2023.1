def fibonacci(n):
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    elif n == 2:
        return 1
    else:
        return 0


for i in range(1, 10):
    print(i, fibonacci(i))
