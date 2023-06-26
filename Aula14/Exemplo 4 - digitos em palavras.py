def num2word(n: int):
    converter = {
        0: "zero", 1: "um", 2: "dois", 3: "tres",
        4: "quatro", 5: "cinco", 6: "seis",
        7: "sete", 8: "oito", 9: "nove"
    }
    return converter[int(n)]


def int_to_words_naive(n: int):
    n_str = str(n)
    converted = [num2word(i) for i in n_str]
    return " ".join(converted)


def int_to_words(n: int):
    if n < 10:
        return num2word(n)
    else:
        composition = " " + num2word(n % 10)
        return int_to_words(n // 10) + composition


print(int_to_words_naive(123))
print(int_to_words(123))