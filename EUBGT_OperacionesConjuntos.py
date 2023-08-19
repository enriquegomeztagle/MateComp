# Find values for each set
is_under_universe_range = lambda value, universe_max_val: value <= universe_max_val
universe_max = 29

S_1 = set()
S_2 = set()
S_3 = set()

calculate_r1 = lambda x: (3 * x + 1) / 2
for x in range(2, 30):
    r = calculate_r1(x)
    if r % 1 == 0 and is_under_universe_range(int(r), universe_max):
        S_1.add(int(r))

calculate_r2 = lambda n: (n ** 2 - 4) / (n - 2)
for n in range(1, 19):
    if n != 2:
        r = calculate_r2(n)
        if r % 1 == 0 and is_under_universe_range(int(r), universe_max):
            S_2.add(int(r))

calculate_r3 = lambda n: (5 * n + 1) / 3
for n in range(3, 20):
    r = calculate_r3(n)
    if r % 1 == 0 and is_under_universe_range(int(r), universe_max):
        S_3.add(int(r))

A = set(filter(lambda e: is_under_universe_range(e, universe_max), S_1))
print("A =", A)

B = set(filter(lambda e: is_under_universe_range(e, universe_max), S_2))
print("B =", B)

C = set(filter(lambda e: is_under_universe_range(e, universe_max), S_3))
print("C =", C)

# Calculate Set Operations
expr1 = (C - A) | (A - C)
expr2 = (A - B) | (B - C)
complement_expr1 = set(range(1, 30)) - expr1
complement_expr2 = set(range(1, 30)) - expr2
final_result1 = complement_expr1 & complement_expr2

print("Result 1) :", final_result1)

intersection_ABC = A & B & C
complement_intersection_ABC = set(range(1, 30)) - intersection_ABC
complement_C = set(range(1, 30)) - C
difference_BC_complement = B - complement_C
expr3 = complement_intersection_ABC - difference_BC_complement
final_result2 = set(range(1, 30)) - expr3

print("Result 2) :", final_result2)

difference_AB = A - B
difference_BC = B - C
difference_CA = C - A
expr4 = difference_AB - difference_BC - difference_CA
complement_A = set(range(1, 30)) - A
complement_B = set(range(1, 30)) - B
expr5 = complement_B & complement_A
final_result3 = expr4 & expr5

print("Result 3) :", final_result3)
