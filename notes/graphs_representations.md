## How to represent graphs in a computer?


Graphs can be represented in at least 3 well known ways, each of them with certain advantages and disadvantages over the others, in terms of time and space complexity, and it terms of implementation effort, etc.

The following are some of the most known graph representations:

1. **Edge List**: We keep 2 lists, one for the vertices, and one for the edges. The list of edges keeps track of 2 pointers to the vertices, which correspond the endpoints of the edge.

2. **Adjacency List**: We keep a list of all the vertices in the graph, and each of this vertices keeps track of a list of its adjacent vertices. Space: O(N + M).
This representation is useful to iterate through the edges. This is probably the most common used implementation.

3. **Adjacency Matrix**: Requires O(n^2) time. We have an n x n matrix, whose entries contain information about the edges, or simply state if between the first vertex and the second there's an edge.