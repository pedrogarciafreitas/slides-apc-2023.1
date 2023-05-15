from factorial import fact
from math import cos as math_cos
from math import fabs

def angle2grads(angulo):
    pi = 3.141592
    return angulo * pi / 180.0


def cos(a, n):
    def cos_it(x, it):
        if it <= 0:
            return 1
        else:
            term = ((-1) ** it) / fact(2*it)
            term *= x ** (2 * it)
            return cos_it(x, it - 1) + term
    x = angle2grads(a)
    return cos_it(x, n)


if __name__ == "__main__":
    n = 5
    valor_fatorial = fact(n)
    print(f"fact({n}) = {valor_fatorial}")
    
    angle = 180
    rad_90 = angle2grads(angle)
    
    print(f"angulo={angle} -> radianos={rad_90}")
    
    cos_value = cos(angle, 20)
    print(f"cos({angle}) = {cos_value}")
    
    for n in range(1, 10, 1):
        my = cos(angle, n)
        bib = math_cos(angle2grads(angle))
        err = fabs(bib-my)
        print(f"n={n} -> our={my}, math={bib}, err={err}")
    