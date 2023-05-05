# Dijkstra算法

from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph, start):
    pq = PriorityQueue()  # 创建一个优先队列对象
    start.setDistance(0)  # 将起始顶点的距离设置为0
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])  # 构建优先队列的堆，使用顶点的距离作为优先级
    while not pq.isEmpty():  # 当优先队列不为空时循环
        currentVert = pq.delMin()  # 从优先队列中删除具有最小距离的顶点
        for nextVert in currentVert.getConnections():  # 遍历当前顶点的相邻顶点
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)  # 计算新的距离
            if newDist < nextVert.getDistance():  # 如果新距离比下一个顶点的距离更小
                nextVert.setDistance(newDist)  # 更新下一个顶点的距离
                nextVert.setPred(currentVert)  # 设置下一个顶点的前驱顶点为当前顶点
                pq.decreaseKey(nextVert, newDist)  # 减小下一个顶点在优先队列中的优先级```

# 代码分析
# 1. 从起始顶点开始，将其距离设置为0，将其加入优先队列中。
# 2. 从优先队列中删除具有最小距离的顶点，遍历该顶点的相邻顶点。
# 3. 对于每个相邻顶点，计算新的距离。如果新距离小于原来的距离，则更新距离，并将前驱顶点设置为当前顶点。
# 4. 将更新后的顶点加入优先队列中。
# 5. 重复步骤2-4，直到优先队列为空。


# 测试
g = Graph()
for i in range(6):
    g.addVertex(i)
g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)
dijkstra(g, g.getVertex(0))
for v in g:
    # 打印每个顶点的前驱顶点和离起始顶点的距离
    print(v.getId(), v.getDistance())
