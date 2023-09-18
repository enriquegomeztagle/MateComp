######## Solve sets
S_1 = set()
for x in range(2,30):
    r = (3*x+1)/2
    if r % 1 == 0:
        S_1.add(int(r))
        # print(r, end=", ")

S_2 = set()
for n in range(1,19):
    if n != 2:
        r = ((n**2-4)/(n-2))
    if r % 1 == 0:
        S_2.add(int(r))
        # print(r, end=", ")

S_3 = set()
for n in range(3,20):
    r = ((5*n+1)/(3))
    if r % 1 == 0:
        S_3.add(int(r))
        # print(r, end=", ")

A = set()
for e in S_1:
    if e <=29:
        # print(e, end=", ")
        A.add(e)
print("A = ", A)

B = set()
for e in S_2:
    if e <=29:
        # print(e, end=", ")
        B.add(e)
print("B = ", B)

C = set()
for e in S_3:
    if e <=29:
        # print(e, end=", ")
        C.add(e)
print("C = ", C)

######## Solve operations

from sympy import symbols, Union, Complement

expr1 = (C - A) | (A - C)
expr2 = (A - B) | (B - C)
complement_expr1 = set(range(1, 30)) - expr1
complement_expr2 = set(range(1, 30)) - expr2
final_result = complement_expr1 & complement_expr2

print("Result 1) :", final_result)

# Calculate the intersection of A, B, and C
intersection_ABC = A & B & C

# Calculate the complement of the intersection of A, B, and C
complement_intersection_ABC = set(range(1, 30)) - intersection_ABC

# Calculate the complement of C
complement_C = set(range(1, 30)) - C

# Calculate the set difference B - C'
difference_BC_complement = B - complement_C

# Calculate the final result of the expression
expr = complement_intersection_ABC - difference_BC_complement
final_result = set(range(1, 30)) - expr

print("Result 2) :", final_result)

# Calculate the set differences
difference_AB = A - B
difference_BC = B - C
difference_CA = C - A

# Calculate the expression [(A - B) - (B - C) - (C - A)]
expr1 = difference_AB - difference_BC - difference_CA

# Calculate the complements of sets A and B
complement_A = set(range(1, 30)) - A
complement_B = set(range(1, 30)) - B

# Calculate the intersection of [B' ∩ A']
expr2 = complement_B & complement_A

# Calculate the final result of the expression
final_result = expr1 & expr2

print("Result 3):", final_result)
