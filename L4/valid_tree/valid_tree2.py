# 判断一个图是否为树，使用并查集

# 查找帮主
def find(x, parent):
    if parent[x] == x:
        return x
    return find(parent[x], parent);

# 将y作为x的父亲节点
def union(x, y, parent):
    parent[x] = y

# 判断一个图是否为树
def valid_tree(n, edges):
    # 初始化节点的父亲节点
    parent = [0 for i in range(n)]
    for i in range(n):
        parent[i] = i

    for edge in edges:
        p1 = find(edge[0], parent)
        p2 = find(edge[1], parent)
        # 两个节点的帮主相等，则说明存在环
        if p1 == p2:
            return False
        # p1是p2的父亲
        union(p2, p1, parent)

    # 如果连通分量为1，那么这些点的帮主都是同一个
    p = find(0, parent)
    for i in range(1,n):
        if p != find(i, parent):
            return False
    return True

print(valid_tree(5, [[0,1], [0,2], [0,3], [1,4]]))
print(valid_tree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
