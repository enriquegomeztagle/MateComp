equation <- function(x) {
  return(x^4 - 5*x^3 - 55*x^2 + 141*x + 630)
}

S_5 <- c()

for (x in 0:999999) {
  if (equation(x) == 0) {
    S_5 <- c(S_5, x)
  }
}

print(S_5)
