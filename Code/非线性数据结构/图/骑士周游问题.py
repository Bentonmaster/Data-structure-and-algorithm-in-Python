# 导入图
from pythonds.graphs import Graph, Vertex

# 骑士周游问题,n为步数，path为路径，u为当前节点，limit为限制步数
def knightTour(n, path, u,  limit):
    u.setColor('gray')
    path.append(u)
    if n < limit:
        nbrList = list(u.getConnections())
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

# 创建棋盘
def knightGraph(bdSize):
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            # 创建节点
            nodeId = posToNodeId(row, col, bdSize)
            # 创建节点的所有可能的下一步的节点
            newPositions = genLegalMoves(row, col, bdSize)
            # 创建边
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

# 将棋盘上的位置转换为节点
def posToNodeId(row, column, board_size):
    return (row * board_size) + column

# 将节点转换为棋盘上的位置
def nodeIdToPos(nodeId, board_size):
    return (nodeId // board_size, nodeId % board_size)

# 生成合法的下一步的位置
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2), (-2,-1), (-2,1),
                   ( 1,-2), ( 1,2), ( 2,-1), ( 2,1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # 判断是否在棋盘内
        if legalCoord(newX, bdSize) and \
                        legalCoord(newY, bdSize):
            newMoves.append((newX, newY))
    return newMoves

# 判断是否在棋盘内
def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False
    
# 测试
knightGraph = knightGraph(8)

# 从(0,0)开始，限制步数为63
path = []
knightTour(0, path, knightGraph.getVertex(0), 63)
for i in path:
    print(nodeIdToPos(i.getId(), 8))


