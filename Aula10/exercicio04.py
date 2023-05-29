# Problema: Dados n pontos no plano, determinar dois deles que estão à
# distância mínima.

def euclidian_distance(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    return ( dx ** 2 + dy ** 2) ** (1/2)


def get_minimal_distance(x, y):
    distance, point1, point2 = None, None, None
    for i in range(1, len(x)):
        for j in range(0, i):
            d = euclidian_distance(x[i], y[i], x[j], y[j])
            if distance is None or d < distance:
                distance = d
                point1 = j
                point2 = i
    return distance, point1, point2


def main():
    n = int(input("Digite a quantidade de pontos: "))
    x, y = [], []
    for i in range(n):
        #a, b = map(int, input(f"Coordenadas do ponto {i+1}: ").split())
        u, v = input(f"Coordenadas do ponto {i+1}: ").split()
        a, b = int(u),int(v)
        x.append(a)
        y.append(b)
    d, p1, p2 = get_minimal_distance(x, y)
    print("Os pontos mais próximos são: ")
    print(f"Ponto {p1+1} ({x[p1]},{y[p1]}) e Ponto {p2+1} ({x[p2]},{y[p2]})")
    print(f"Distancia={d:.2f}")



if __name__ == "__main__":
    main()