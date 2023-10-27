sieve_of_eratosthenes <- function(n) {
  if (is.na(n) || n < 0) {
    cat("Please enter a valid positive number.\n")
    return()
  } else if (n == 0 || n == 1) {
    cat(paste("No prime numbers until", n, ".\n"))
    return()
  }
  
  if (n >= 2) {
    cat(2)
  }
  if (n >= 3) {
    cat(' ', 3, sep = '')
  }
  
  max <- (n-3)/2
  is_prime_vec <- rep(TRUE, max)
  
  i <- 0
  while ((2*i+3)*(2*i+3) <= n) {
    if (is_prime_vec[i]) {
      k <- 1  # Initialize k here.
      while ((2*k+1)*(2*i+3) <= n) {
        is_prime_vec[((2*k+1)*(2*i+3)-3)/2] <- FALSE
        k <- k + 1        
      }
    }
    i <- i + 1
  }
  
  # Removing the repeated 2, 3 printing.
  
  for (j in 1:max) {
    if (is_prime_vec[j]) {
      cat(' ', 2*j+3, sep = '')
    }
  }
  cat("\n")
}

cat("Enter a number: ")
number <- as.integer(readline(prompt=""))
if (is.na(number)) {
  cat("Please enter a valid number.\n")
} else {
  sieve_of_eratosthenes(number)
}
