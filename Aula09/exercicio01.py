# Check format strings at https://pyformat.info/#simple

def print_name(name: str):
    sentence = f"Hola, {name}"
    width = len(sentence)
    bar = '-' * width
    print("bar=", bar, width)
    print('+-' + bar + '-+')
    print('| {code:^{length}} |'.format(code="", length=width))
    print('| {sentence:^{width}} |'.format(sentence=sentence, width=width))
    print('| {code:^{length}} |'.format(code="", length=width))
    print('+-' + '-'*(width) + '-+')


print_name("Pablo")

