def get_zeros_naive(n: int):
    n_str = str(n)
    n_list = list(n_str)
    zeroes = sum([1 for i in n_list if i == '0'])
    return zeroes


def get_zeros_naive2(n: int):
    n_str = str(n)
    zeroes = n_str.count('0')
    return zeroes


def get_zeros(n: int):
    if n == 0:
        return 1
    elif n < 10 and n != 0:
        return 0
    elif n % 10 == 0:
        return get_zeros(n // 10) + 1
    else:
        return get_zeros(n // 10)


print(get_zeros_naive(2030))
print(get_zeros_naive2(2030))
print(get_zeros(2030))