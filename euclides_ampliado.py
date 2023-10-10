def euclides_ampliado(a, b):
    c, d = abs(a), abs(b)
    c1, d1 = 1, 0
    c2, d2 = 0, 1

    while d:
        q = c // d
        c, d = d, c - q * d
        c1, d1 = d1, c1 - q * d1
        c2, d2 = d2, c2 - q * d2

    s = c1 * (1 if a > 0 else -1)
    t = c2 * (1 if b > 0 else -1)
    return c, s, t

a = 120
b = 20
mcd, s, t = euclides_ampliado(a, b)

print(f"MCD: {mcd}, s: {s}, t: {t}")
