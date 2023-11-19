install.packages("igraph")

library(igraph)

# Define the set A because A = B
A <- c(1, 2, 3, 4, 5, 6, 7, 8)

# Initialize a matrix for the relation R with zeros
R_matrix <- matrix(0, nrow=length(A), ncol=length(A))

# Fill the matrix according to the given condition of the relation 5 <= a + b <= 7
for (i in 1:length(A)) {
  for (j in 1:length(A)) {
    if (5 <= A[i] + A[j] && A[i] + A[j] <= 7) {
      R_matrix[i, j] <- 1
    }
  }
}

# Print the R matrix
print(R_matrix)

# OUTPUT:
#      [,1] [,2] [,3] [,4] [,5] [,6] [,7] [,8]
# [1,]    0    0    0    1    1    1    0    0
# [2,]    0    0    1    1    1    0    0    0
# [3,]    0    1    1    1    0    0    0    0
# [4,]    1    1    1    0    0    0    0    0
# [5,]    1    1    0    0    0    0    0    0
# [6,]    1    0    0    0    0    0    0    0
# [7,]    0    0    0    0    0    0    0    0
# [8,]    0    0    0    0    0    0    0    0

# Create the graph from the adjacency matrix
g <- graph_from_adjacency_matrix(R_matrix, mode="directed", diag=FALSE)

# Plot the graph
plot(g, layout=layout_in_circle, vertex.size=30, vertex.label=c(1:8), 
     edge.arrow.size=0.5, main="Directed Graph of the Relation R")