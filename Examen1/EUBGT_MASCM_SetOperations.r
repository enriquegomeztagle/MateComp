cat("Set results\n")

# Universe definition
U <- -9:13

# Define values for each set
is_in_universe <- function(value) {
  return(value %in% U)
}

# A: (5x-3)/2 for -8 < x <= 12 and x in Z
A_values <- integer(0)
for (x in (-7):12) {
  r <- (5 * x - 3) / 2
  if (r %% 1 == 0 && is_in_universe(r)) {
    A_values <- c(A_values, as.integer(r))
  }
}

# B: (5n-7)/3 for -7 < n < 14 and n in Z
B_values <- integer(0)
for (n in (-6):13) {
  r <- (5 * n - 7) / 3
  if (r %% 1 == 0 && is_in_universe(r)) {
    B_values <- c(B_values, as.integer(r))
  }
}

# C: (y²-4)/(y-2) for -7 <= y <= 12 and y != 2
C_values <- integer(0)
for (y in (-7):12) {
  if (y != 2) {
    r <- (y^2 - 4) / (y - 2)
    if (r %% 1 == 0 && is_in_universe(r)) {
      C_values <- c(C_values, as.integer(r))
    }
  }
}

# D: values of x for which x⁴+7x³+5x²-31x-30=0
equation_D <- function(x) {
  return(x^4 + 7*x^3 + 5*x^2 - 31*x - 30)
}

D_values <- U[which(equation_D(U) == 0)]

# Print initial set results
cat("A =", sort(A_values), "\n")
cat("B =", sort(B_values), "\n")
cat("C =", sort(C_values), "\n")
cat("D =", sort(D_values), "\n\n")

# Steps

# 1. C intersection B
step_1 <- intersect(C_values, B_values)

# 2. B - D
step_2 <- setdiff(B_values, D_values)

# 3. Complement of (B - D)
step_3 <- setdiff(U, step_2)

# 4. Symmetric difference between (C intersection B) and complement of (B - D)
step_4 <- setdiff(union(step_1, step_3), intersect(step_1, step_3))

# 5. C - A
step_5 <- setdiff(C_values, A_values)

# 6. A intersection B
step_6 <- intersect(A_values, B_values)

# 7. Union of (C - A) and (A intersection B)
step_7 <- union(step_5, step_6)

# 8. Union of step 4 and step 7
step_8 <- union(step_4, step_7)

# 9. B - A
step_9 <- setdiff(B_values, A_values)

# 10. A - C
step_10 <- setdiff(A_values, C_values)

# 11. Complement of (A - C)
step_11 <- setdiff(U, step_10)

# 12. Symmetric difference between (B - A) and its complement
step_12 <- setdiff(union(step_9, step_11), intersect(step_9, step_11))

# 13. Complement of (A union B)
step_13 <- setdiff(U, union(A_values, B_values))

# 14. Final expression result
result <- setdiff(setdiff(step_8, step_12), step_13)

# Print the results
cat("\nStep by step calculations\n")
cat("1. C intersection B:", sort(step_1), "\n")
cat("2. B - D:", sort(step_2), "\n")
cat("3. Complement of (B - D):", sort(step_3), "\n")
cat("4. Symmetric difference of (C intersection B) and complement of (B - D):", sort(step_4), "\n")
cat("5. C - A:", sort(step_5), "\n")
cat("6. A intersection B:", sort(step_6), "\n")
cat("7. Union of (C - A) and (A intersection B):", sort(step_7), "\n")
cat("8. Union of results from step 4 and step 7:", sort(step_8), "\n")
cat("9. B - A:", sort(step_9), "\n")
cat("10. A - C:", sort(step_10), "\n")
cat("11. Complement of (A - C):", sort(step_11), "\n")
cat("12. Symmetric difference of (B - A) and (A-C)':", sort(step_12), "\n")
cat("13. Complement of (A union B):", sort(step_13), "\n")
cat("14. Final Result:", sort(result), "\n")
