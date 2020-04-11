# 判断一个图是否为树，使用DFS
def valid_tree(n, edges):
    # 若这个图的边数比n-1多，那么一定有环，如果比n-1小，有孤立点
    if len(edges) != n - 1: 
        return False
    
    # 初始化邻接表
    mat =[[] for i in range(n)]
    for i in range(len(edges)):
        v, u = edges[i][0], edges[i][1]
        mat[v].append(u)
        mat[u].append(v)

    # 判定这棵树的连通分量是否为1
    count = 0
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            dfs(i, visit, mat)
            # 统计连通图的个数
            count = count + 1

    if count > 1: 
        return False
    return True

# 深度优先遍历
def dfs(node, visit, mat):
    # 访问过的节点不再进行访问
    visit[node] = 1
    for i in range(len(mat[node])):
        neighbor = mat[node][i]
        if visit[neighbor] == 0:
            dfs(neighbor, visit, mat)

print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(valid_tree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
