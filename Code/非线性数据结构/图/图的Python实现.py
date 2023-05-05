# ADT Graph:
#   Graph(self)                     # 构造函数
#   addVertex(self, key)            # 添加顶点
#   addEdge(self, fromVert, toVert) # 添加边
#   addEdge(self, fromVert, toVert, weight) # 添加带权边
#   getVertex(self, key)            # 获取顶点
#   getVertices(self)               # 获取所有顶点

# Python实现
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
    
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key): # 添加顶点
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, key): # 获取顶点
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None
        
    def __contains__(self, key): # 重载in操作符
        return key in self.vertList
    
    def addEdge(self, fromVert, toVert, weight=0): # 添加边
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertices(self): # 获取所有顶点
        return self.vertList.keys()

    def __iter__(self): # 重载迭代器
        return iter(self.vertList.values())
    
    def __str__(self): # 重载str操作符
        return str(self.vertList)
    
# 测试  
g = Graph()
for i in range(6):
    g.addVertex(i)
print(g.vertList)
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))

# 有向图
class Digraph(Graph):
    def addEdge(self, fromVert, toVert, weight=0): # 添加边
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

# 无向图
class UnDigraph(Graph):
    def addEdge(self, fromVert, toVert, weight=0): # 添加边
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)
        self.vertList[toVert].addNeighbor(self.vertList[fromVert], weight)

