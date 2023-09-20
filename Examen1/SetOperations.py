print("Set results")

# Universe definition
U = set(range(-9, 14))  # The set of integers from -9 to 13, inclusive

# Find values for each set
is_in_universe = lambda value: value in U

A_values = set()
B_values = set()
C_values = set()
D_values = set()

# A: (5x-3)/2 for -8 < x <= 12 and x in Z
calculate_A = lambda x: (5 * x - 3) / 2
for x in range(-7, 13):  # We start from -7 since -8 is not included
    r = calculate_A(x)
    if r.is_integer() and is_in_universe(int(r)):
        A_values.add(int(r))

# B: (5n-7)/3 for -7 < n < 14 and n in Z
calculate_B = lambda n: (5 * n - 7) / 3
for n in range(-6, 14):  # We start from -6 and end at 13 since -7 and 14 are not included
    r = calculate_B(n)
    if r.is_integer() and is_in_universe(int(r)):
        B_values.add(int(r))

# C: (y²-4)/(y-2) for -7 <= y <= 12 and y != 2
calculate_C = lambda y: (y**2 - 4) / (y - 2)
for y in range(-7, 13):  # We go till 12 since 12 is included
    if y != 2:  # y should not be 2, as the denominator cannot be zero
        r = calculate_C(y)
        if r.is_integer() and is_in_universe(int(r)):
            C_values.add(int(r))

# D: values of x for which x⁴+7x³+5x²-31x-30=0
equation_D = lambda x: x**4 + 7*x**3 + 5*x**2 - 31*x - 30
for x in U:
    if equation_D(x) == 0:
        D_values.add(x)

# Print initial set results
print("A =", sorted(A_values))
print("B =", sorted(B_values))
print("C =", sorted(C_values))
print("D =", sorted(D_values))

# Steps

# 1. C intersection B
step_1 = C_values.intersection(B_values)

# 2. B - D
step_2 = B_values.difference(D_values)

# 3. Complement of (B - D)
step_3 = U.difference(step_2)

# 4. Symmetric difference between (C intersection B) and complement of (B - D)
step_4 = step_1.symmetric_difference(step_3)

# 5. C - A
step_5 = C_values.difference(A_values)

# 6. A intersection B
step_6 = A_values.intersection(B_values)

# 7. Union of (C - A) and (A intersection B)
step_7 = step_5.union(step_6)

# 8. Union of step 4 and step 7
step_8 = step_4.union(step_7)

# 9. B - A
step_9 = B_values.difference(A_values)

# 10. A - C
step_10 = A_values.difference(C_values)

# 11. Complement of (A - C)
step_11 = U.difference(step_10)

# 12. Symmetric difference between (B - A) and its complement
step_12 = step_9.symmetric_difference(step_11)

# 13. Complement of (A union B)
step_13 = U.difference(A_values.union(B_values))

# 14. Final expression result
result = step_8.difference(step_12).difference(step_13)

# Print the results
print("\n\nStep by step calculations")
print("1. C intersection B:", sorted(step_1))
print("2. B - D:", sorted(step_2))
print("3. Complement of (B - D):", sorted(step_3))
print("4. Symmetric difference of (C intersection B) and complement of (B - D):", sorted(step_4))
print("5. C - A:", sorted(step_5))
print("6. A intersection B:", sorted(step_6))
print("7. Union of (C - A) and (A intersection B):", sorted(step_7))
print("8. Union of results from step 4 and step 7:", sorted(step_8))
print("9. B - A:", sorted(step_9))
print("10. A - C:", sorted(step_10))
print("11. Complement of (A - C):", sorted(step_11))
print("12. Symmetric difference of (B - A) and (A-C)':", sorted(step_12))
print("13. Complement of (A union B):", sorted(step_13))
print("14. Final Result:", sorted(result))
