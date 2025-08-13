visited = []
tower = []

def make_tree(num):
    global visited, tower
    
    visited[num] = 1
    for i in tower[num]:
        if visited[i] == 0:
            make_tree(i)

def solution(n, wires):
    global visited, tower
    
    possible = []
    for i in range(n - 1):
        tower = [[] for i in range(n + 1)]
        visited = [0 for i in range(n + 1)]
        
        for j in range(n - 1):
            if i == j:
                continue
            else:
                tower[wires[j][0]].append(wires[j][1])
                tower[wires[j][1]].append(wires[j][0])
                
        make_tree(1)
        
        value = 0
        for i in range(1, n + 1):
            if visited[i] == 0:
                value += 1
        
        possible.append(value)
    
    values = [abs(x - (n - x)) for x in possible]
    
    return min(values)