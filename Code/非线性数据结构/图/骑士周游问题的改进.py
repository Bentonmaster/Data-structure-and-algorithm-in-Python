from pythonds.graphs import Graph, Vertex

# 骑士周游算法的改进（仅修改了遍历下一格的顺序，nbrList = orderByAvail(u)）
# 1. 限制步数
# 2. Warnsdorff算法
# Warnsdorff算法：从当前节点出发，选择下一步的节点时，选择下一步的节点的出度最小的节点
# 3. 优化Warnsdorff算法
# Warnsdorff算法的问题：当有多个节点的出度相同时，选择下一步的节点时，会随机选择一个节点，这样会导致搜索的路径不是最短路径
# 优化：当有多个节点的出度相同时，选择下一步的节点时，选择下一步的节点的入度最小的节点

# 创建骑士周游问题的棋盘
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

def nodeIdToPos(nodeId, board_size):
    return (nodeId // board_size, nodeId % board_size)

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2), (-2,-1), (-2,1),
                   ( 1,-2), ( 1,2), ( 2,-1), ( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and \
                        legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

# Warnsdorff算法
def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c += 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


# 骑士周游算法
def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        # 使用Warnsdorff算法
        # nbrList = orderByAvail(u)
        # 使用优化后的Warnsdorff算法
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i += 1
        if not done: # prepare to backtrack
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

# 测试
ktGraph = knightGraph(8)
path = []
knightTour(0, path, ktGraph.getVertex(0), 63)
for v in path:
    print(v.getId())


