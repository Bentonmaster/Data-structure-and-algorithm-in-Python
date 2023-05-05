# BFS 广度优先搜索算法
from pythonds.graphs import Graph, Vertex
from collections import deque

# 导入函数buildGraph
def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g

def bfs(g,start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = deque()
    vertQueue.append(start)
    while (len(vertQueue) > 0):
        currentVert = vertQueue.popleft()
        for nbr in currentVert.getConnections(): # nbr: neighbor
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.append(nbr)
        currentVert.setColor('black')

# 回溯函数
def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

wordGraph = buildGraph('Code/非线性数据结构/图/fourletterwords.txt')
bfs(wordGraph, wordGraph.getVertex('FOOL'))
traverse(wordGraph.getVertex('BULK'))




