install.packages("igraph")

library(igraph)

# Define the set A because A = B
A <- c(1, 2, 3, 4, 5)

# Initialize a matrix for the relation R with zeros
R_matrix <- matrix(0, nrow=length(A), ncol=length(A))

# Define the pairs that are in the relation R
relation_pairs <- list(c(1, 1), c(1, 2), c(1, 5), c(2, 1), c(2, 2), c(2, 5),
                       c(3, 3), c(3, 4), c(4, 3), c(4, 4), c(5, 1), c(5, 2), c(5, 5))

# Fill the matrix according to the given relation R
for (pair in relation_pairs) {
  R_matrix[pair[[1]], pair[[2]]] <- 1
}

# Print the R matrix
print(R_matrix)

# Create the graph from the adjacency matrix
g <- graph_from_adjacency_matrix(R_matrix, mode="directed", diag=TRUE)

# Plot the graph
plot(g, layout=layout_in_circle, vertex.size=30, vertex.label=c(1:length(A)), 
     edge.arrow.size=0.5, main="Directed Graph of the Relation R")
