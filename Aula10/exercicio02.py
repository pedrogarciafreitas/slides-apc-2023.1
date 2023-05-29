# 2. Interpretador louco: Você ficou encarregado de escrever um interpretador
# que realiza operações binárias entre dois números inteiros positivos de 8
# bits. Seu interpretador possui uma instruction set architecture reduzida,
# contendo apenas as instruções binárias XOR, OR, e AND. Contudo, antes de
# realizar essas operações o seu interpretador inverte um bit aleatoriamente
# nos números de entrada. Escreva um programa que recebe dois números
# inteiros, converta-os para represetação binária, inverta um bit aleatório
# desses operandos e realize as operações XOR, OR, e AND. Por fim, exiba os
# números  lidos, suas representações binárias, os bits invertidos, os novos
# números gerados a partir desses bits invertidos e o valor das operações.


def get_nth_bit(binary, position):
    shifted_one = 0x01 << position
    bit_at_position = binary & shifted_one
    return bit_at_position >> position


def set_bit(binary, bit_position):
    return binary | (1 << bit_position)


def clear_bit(binary, bit_position):
    return binary & ~(1 << bit_position)


def invert_nth_bit(binary, position):
    bit = get_nth_bit(binary, position)
    if bit:
        return clear_bit(binary, position)
    else:
        return set_bit(binary, position)


def invert_random_bit(binary_number):
    import random
    #random.seed(0)
    position = random.randint(0, 8)
    return invert_nth_bit(binary_number, position)


def decimal2binary(decimal):
    binary = bin(decimal)
    str_formatting = binary[2:].zfill(8)
    return str_formatting


def get_bit_diffs(num1, num2):
    return num1 ^ num2


def main():
    x,y = map(int, input().split(" "))

    invx, invy = map(invert_random_bit, (x, y))
#     (invx2, invy2) = (invert_random_bit(x), invert_random_bit(y))
#     for i in (x,y):
#         inv = invert_random_bit(i)
#         print("inv->", inv)
#     
#     print("mapped -> ", invx, invy)
#     print("tuple ->", invx2, invy2)
#     
#     exit(0)
    
    and_result = invx & invy
    or_result = invx | invy
    xor_result = invx ^ invy
    fmt_tabular = "{:<22} | {:<8} | {:<8}"
    
    print(fmt_tabular.format("inputs: ", x, y))
    u,v = map(decimal2binary, (x, y))
    invu, invv = map(decimal2binary, (invx, invy))
    print(fmt_tabular.format("binary equivalents:", u, v))

    dec_invx = decimal2binary(invx)
    dec_invy = decimal2binary(invy)
    print(fmt_tabular.format("inverted equivalents:", dec_invx, dec_invy))

    diff_x = get_bit_diffs(x, invx)
    diff_y = get_bit_diffs(y, invy)
    dec_diff_x = decimal2binary(diff_x)
    dec_diff_y = decimal2binary(diff_y)
    print(fmt_tabular.format("binary diffs:", dec_diff_x, dec_diff_y))
    
    print(f"XOR({invu},{invv})={decimal2binary(xor_result)}")
    print(f"OR({invu},{invv})={decimal2binary(or_result)}")
    print(f"AND({invu},{invv})={decimal2binary(and_result)}")


if __name__ == "__main__":
    main()