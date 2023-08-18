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

R_1 = []
for e in S_1:
    if e <=29:
        # print(e, end=", ")
        R_1.append(e)
print("A = ", R_1)

R_2 = []
for e in S_2:
    if e <=29:
        # print(e, end=", ")
        R_2.append(e)
print("B = ", R_2)

R_3 = []
for e in S_3:
    if e <=29:
        # print(e, end=", ")
        R_3.append(e)
print("C = ", R_3)
