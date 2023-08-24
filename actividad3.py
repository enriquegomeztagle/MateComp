##### Find values for each set
universe_min = 2
universe_max = 11
is_under_universe_range = lambda value, universe_max_val: value <= universe_max_val
is_above_universe_range = lambda value, universe_min_val: value >= universe_min_val

print("Find set values")
A = set()
calculate_a = lambda x: (3 * x + 1) / (2)
for x in range(universe_min, universe_max):
    r = calculate_a(x)
    if r % 1 == 0:
        A.add(int(r))

A = set(filter(lambda e: is_under_universe_range(e, universe_max), A))
print("A =", A)

B = set()
calculate_b = lambda n: (7 * n + 2) / (5)
for n in range(3, 9):
    r = calculate_b(n)
    if r % 1 == 0:
        B.add(int(r))

B = set(filter(lambda e: is_above_universe_range(e, universe_min), B))
print("B =", B)

C = set()
calculate_c = lambda y: (y**2 - 9) / (y - 3)
for y in range(1, 9):
    if y != 3:
        r = calculate_c(y)
        if r % 1 == 0:
            C.add(int(r))

C = set(filter(lambda e: is_under_universe_range(e, universe_max), C))
print("C =", C)

# D condition is the equation x**2 - x - 56 = 0, we can't use lambda function because it's not a function, it is an equation, have a boolean variable
D = set()
for x in range(2, 11 + 1):
    if x**2 - x - 56 == 0:
        D.add(x)
    else:
        pass

D = set(filter(lambda e: is_under_universe_range(e, universe_max), D))
print("D =", D)

##### Solve set operations
print("-----------\nSet operations")
print("\na)")
uni_a_b = A.union(B)
print("A | B =", sorted(uni_a_b))
complement_uni_a_b = set(range(universe_min, universe_max)) - uni_a_b
print("(A | B)' =", sorted(complement_uni_a_b))
diff_d_c = D.difference(C)
print("D - C =", sorted(diff_d_c))
complement_diff_d_c = set(range(universe_min, universe_max)) - diff_d_c
print("(D - C)' =", sorted(complement_diff_d_c))
final_o1 = complement_uni_a_b - complement_diff_d_c
print("FINAL RESULT: (A | B)' - (D - C)' =", sorted(final_o1))

print("\nb)")
inter_c_d = C.intersection(D)
print("C & D =", sorted(inter_c_d))
complement_inter_c_d = set(range(universe_min, universe_max)) - inter_c_d
print("(C & D)' =", sorted(complement_inter_c_d))
complement_b = set(range(universe_min, universe_max)) - B
print("(B)' =", sorted(complement_b))
final_o2 = complement_inter_c_d.symmetric_difference(complement_b)
print("FINAL RESULT: (C & D)' Δ (B)' =", sorted(final_o2))

print("\nc)")
complement_c = set(range(universe_min, universe_max)) - C
print("(C)' =", sorted(complement_c))
sym_diff_d_a = D.symmetric_difference(A)
print("(D ∆ A) =", sorted(sym_diff_d_a))
final_o3 = complement_c - sym_diff_d_a
print("FINAL RESULT: (C)' - (D ∆ A) =", sorted(final_o3))


print("\nd)")
uni_a_b_com = A.union(complement_b)
print("A | (B)' =", sorted(uni_a_b_com))
diff_uni_a_b_com_c = uni_a_b_com.difference(C)
print("(A | (B)' - C) =", sorted(diff_uni_a_b_com_c))
complement_d = set(range(universe_min, universe_max)) - D
final_o4 = diff_uni_a_b_com_c.symmetric_difference(complement_d)
print("FINAL RESULT: (A | (B)' - C) Δ (D) =", sorted(final_o4))