def isFeasible(n, graph, colors, c):
    # Iterate trough adjacent vertices
    # and check if the vertex color is different from c
    for i in range(n):
        if graph[n][i] and (solutionList[i]==c):
            return False
    return True

# n = vertex nb
def graphColoring(graph, colors, n):
    # Check if all vertices are assigned a color
    if len(colors)+1 == n :
        return True

    # Trying differents color for the vertex n
    for c in colors:
        # Check if assignment of color c to n is possible
        if isFeasible(n, graph, colors, c):
            # Assign color c to n
            solutionList[n] = c
            # Recursively assign colors to the rest of the vertices
            if graphColoring(graph, colors, n+1):
                return True

            else:
                solutionList[n] = 0




colors = ['r', 'g', 'b']

graph = [[False, True, False, False, False, True],
[True, False, True, False, False, True ],
[False, True, False, True, True, False],
[False, False, True, False, True, False],
[False, False, True, True, False, True ],
[True, True, False, False, True, False]]

n=len(graph)
solutionList = [False] * n
#beginning with vertex 0
if graphColoring(graph, colors, 0):
    print (solutionList)
else:
    print ("No solutions")
