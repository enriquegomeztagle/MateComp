# Install and load the 'numbers' library
install.packages("numbers")
library(numbers)

# Define the Mersenne number function
mersenne <- function(n) {
  return(2^n - 1)
}

# Initialize a list to store Mersenne numbers
mersenne_numbers <- c()

# Generate Mersenne numbers up to a certain exponent
max_exponent <- 10
for (n in 1:max_exponent) {
  m <- mersenne(n)
  mersenne_numbers <- c(mersenne_numbers, m)
  cat("Mersenne number with exponent", n, ":", m, "\n")
}

cat("Generated Mersenne numbers:", mersenne_numbers, "\n")
