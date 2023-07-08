def dfs(node, vis, topo, ar):
    vis[node] = True
    
    for i in ar[node]:
        if vis[i] == False:
            dfs(i, vis, topo, ar)
    
    topo.append(node)

def bfs(indegree, ar, n):
    q = []

    for i in range(1, n+1):
        if indegree[i] == 0: 
            q.append(i)
    
    topoTasks = [] 

    while len(q) != 0:
        sz = len(q)
        curr = []
        for i in range(sz):
            node = q[0]
            q.pop(0)
            curr.append(node)
            for j in ar[node]:
                indegree[j] -= 1 
                if indegree[j] == 0: 
                    q.append(j)
        topoTasks.append(curr)

    return topoTasks

def isTopoSortValid(topo, edges):
    pos = {}
    for i in range(len(topo)):
        pos[topo[i]] = i 
    
    for edge in edges:
        if pos[edge[0]] > pos[edge[1]]:
            return False

    return True


def topoSort(n, ar):
    vis = {}
    edges = []
    indegree = [0]*(n+1)

    for i in range(1, n+1):
        for j in ar[i]:
            edges.append([i, j])
            indegree[j] += 1 

    for i in range(n+1):
        vis[i] = False
        
    topo = []
    for i in range(1,n+1): 
        if vis[i] == False:
            dfs(i, vis, topo, ar)
    topo.reverse()

    if isTopoSortValid(topo, edges):
        topoTasks = bfs(indegree, ar, n)
        return topoTasks 
    else : 
        return []
    

if __name__ == '__main__':
    print("Running topoSort.py")