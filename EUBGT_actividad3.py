##### Part 1
##### Find values for each one of the sets
print("PART 1")
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

##### Part 3
# Define sets
print("PART 3")
A = {12, 3, 10, 14, 6, 16, 7, 9, 1}
B = {11, 2, 8, 4, 1, 7, 9, 6, 16}
C = {3, 10}
D = {1, 7}
E = {7, 9}
F = {2, 8}
G = {5}
U = set()
U.update(A)
U.update(B)
U.update(C)
U.update(D)
U.update(E)
U.update(F)
U.update(G)
U.update({13, 15})

print("-----------\nSet operations")


def complement(s):
    return set(range(1, 16)) - s


# We need to say true or false for each premise, print V or F for each
if F.issubset(B - A):
    print("F ⊆ (B-A): ", True)
else:
    print("F ⊆ (B-A) =", False)

if A.intersection(C) == set():
    print("A ∩ C = ∅: ", True)
else:
    print("A ∩ C = ∅: ", False)

if E.difference(D) == set({9}):
    print("E - D = {9}: ", True)
else:
    print("E - D = {9}: ", False)

if E.intersection(D) == set():
    print("E ∩ D = ∅:", True)
else:
    print("E ∩ D = ∅:", False)

if C.union(E).issubset(B):
    print("(C ∪ E) ⊆ B: ", True)
else:
    print("(C ∪ E) ⊆ B: ", False)

if D.difference(E).issubset(A.intersection(B)):
    print("(D - E) ⊆ (A ∩ B): ", True)
else:
    print("(D - E) ⊆ (A ∩ B): ", False)

if C.difference(G) == {3, 10}:
    print("(C - G) = {3,10}: ", True)
else:
    print("(C - G) = {3,10}: ", False)

if G.difference(F) == set():
    print("(G - F) = ∅: ", True)
else:
    print("(G - F) = ∅: ", False)

if F.difference(C).issubset(B):
    print("(F - C) ⊆ B: ", True)
else:
    print("(F - C) ⊆ B: ", False)

if A.difference(B) == {3, 10, 12, 14}:
    print("(A - B) = {3,10,12,14}: ", True)
else:
    print("(A - B) = {3,10,12,14}: ", False)

if D.intersection(E) == {1, 7, 9}:
    print("(D ∩ E) = {1,7,9}: ", True)
else:
    print("(D ∩ E) = {1,7,9}: ", False)

if D.intersection(E).issubset(A.union(B)):
    print("(D ∩ E) ⊆ (A ∪ B): ", True)
else:
    print("(D ∩ E) ⊆ (A ∥ B): ", False)

if 16 not in (D.union(E)):
    print("16 ∉ (D ∪ E): ", True)
else:
    print("16 ∉ (D ∩ E): ", False)

if complement(A.union(B)) == {5, 13, 15}:
    print("(A ∪ B)' = {5,13,15}: ", True)
else:
    print("(A ∪ B)' = {5,13,15}: ", False)

if B.difference(A) == {2, 4, 8, 11}:
    print("(B - A) = {2,4,8,11}: ", True)
else:
    print("(B - A) = {2,4,8,11}: ", False)

if A.intersection(B).union(A.difference(B)) == A:
    print("(A ∩ B) ∪ (A - B) = A: ", True)
else:
    print("(A ∩ B) ∪ (A - B) = A: ", False)

if 2 in complement(U):
    print("2 ∈ U': ", True)
else:
    print("2 ∈ U': ", False)

if (U - (A.union(B))) == G.union({13, 15}):
    print("(U - (A ∩ B)) = G ∪ {13,15}: ", True)
else:
    print("(U - (A ∩ B)) = G ∪ {13,15}: ", False)

if D.symmetric_difference(E) == {1, 9}:
    print("(D ∆ E) = {1,9}: ", True)
else:
    print("(D ∆ E) = {1,9}: ", False)

if A.difference(A.intersection(B)) == C.union({12, 14}):
    print("(A - (A ∩ B)) = C ∪ {12,14}: ", True)
else:
    print("(A - (A ∩ B)) = C ∪ {12,14}: ", False)
