def equation(x):
    return x**4 - 5*x**3 - 55*x**2 + 141*x + 630

S_5 = set()

for x in range(0, 1000000):
    if equation(x) == 0:
        S_5.add(x)

print(S_5)
