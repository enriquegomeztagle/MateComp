find_primes <- function(n) {
  if (n <= 0) {
    stop("Please enter a positive number.")
  } else if (n %in% c(1, 2, 3)) {
    stop("The number should be greater than 3.")
  }
  
  max_val <- (n - 3) %/% 2
  is_prime <- rep(TRUE, max_val + 1)
  
  i <- 0
  while ((2 * i + 3) * (2 * i + 3) <= n) {
    k <- i + 1
    if (is_prime[i + 1]) {
      while ((2 * k + 1) * (2 * i + 3) <= n) {
        is_prime[((2 * k + 1) * (2 * i + 3) - 3) %/% 2 + 1] <- FALSE
        k <- k + 1
      }
    }
    i <- i + 1
  }
  
  
  primes <- c(2, 3)
  for (j in 2:(max_val + 1)) {
    if (is_prime[j]) {
      primes <- c(primes, 2 * (j - 1) + 3)
    }
  }
  
  cat(paste(primes, collapse = ", "), "\n")
}


input_num <- as.integer(readline(prompt="Please enter a positive integer: "))

if (is.na(input_num)) {
  cat("Invalid input. Please enter a positive integer.\n")
} else {
  find_primes(input_num)
}
