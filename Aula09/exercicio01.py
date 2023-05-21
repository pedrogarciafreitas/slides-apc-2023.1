
def print_name(name: str):
    sentence = f"Ola, {name}"
    width = len(sentence)
    print('+-' + '-' * width + '-+')
    print('| {code:^{length}} |'.format(code="", length=width))
    print('| {sentence:^{width}} |'.format(sentence=sentence, width=width))
    print('| {code:^{length}} |'.format(code="", length=width))
    print('+-' + '-'*(width) + '-+')


print_name("Alexandre")

