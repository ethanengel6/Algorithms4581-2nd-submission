def isFeasible(row, solutionList, color):
        for i in range(len(row)):
            if (row[i]==True and solutionList[i]==color):
                return False
        return True


def colorRecursion(graph, solutionList, index):
    n=len(graph)
    if index == n:
        return True
    for c in colors:
        if isFeasible(graph[index], solutionList, c):
            solutionList[index] = c
            if colorRecursion(graph,solutionList, index + 1):
                return True
            solutionList[index] = None
    return False


def color(graph):
    n=len(graph)
    solutionList = [None] * n
    if colorRecursion(graph, solutionList, 0):
        return solutionList
    return False


graph = [[False, True, False, False, True, True ],
[True, False, False, True True, False ],
[False, False, False, True, True, False],
[False, True, True, False, False, False],
[True, True, True, False, False, True ],
[True, False, False, False, True, False]]

colors=['r','g','b']
print(color(graph))
