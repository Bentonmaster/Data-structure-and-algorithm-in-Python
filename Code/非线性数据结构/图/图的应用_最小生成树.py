# prim算法：最小生成树

from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys

def prim(aGraph, start):
    pq = PriorityQueue()  # 创建一个优先队列对象
    for v in aGraph:  # 遍历图中的所有顶点
        v.setDistance(sys.maxsize)  # 将所有顶点的距离设置为无穷大
        v.setPred(None)  # 将所有顶点的前驱顶点设置为None
    start.setDistance(0)  # 将起始顶点的距离设置为0
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])  # 构建优先队列的堆，使用顶点的距离作为优先级
    while not pq.isEmpty():  # 当优先队列不为空时循环
        currentVert = pq.delMin()  # 从优先队列中删除具有最小距离的顶点
        for nextVert in currentVert.getConnections():  # 遍历当前顶点的相邻顶点
            newCost = currentVert.getWeight(nextVert)  # 计算新的权重
            if nextVert in pq and newCost < nextVert.getDistance():  # 如果新权重比下一个顶点的权重更小
                nextVert.setPred(currentVert)  # 设置下一个顶点的前驱顶点为当前顶点
                nextVert.setDistance(newCost)  # 更新下一个顶点的距离
                pq.decreaseKey(nextVert, newCost)  # 减小下一个顶点在优先队列中的优先级

# Dijkstra算法通过选择与起始节点距离最小的节点来逐步扩展最短路径树，
# 而Prim算法通过选择与当前已选节点集合距离最小的节点来逐步构建最小生成树。

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
prim(g, g.getVertex(0))
for v in g:
    print(v.getId(), v.getDistance())
