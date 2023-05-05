from collections import deque
# 从标准输入中读取输入数据
M = int(input())
n = int(input())
points = []
for _ in range(n):
    xi, yi = map(int, input().split())
    points.append([xi, yi])

# 创建一个优化后的循环，用于处理每个点
def find_min_days(M, n, points):
    # 创建一个布尔值列表，用于标记已经访问过的节点
    visited = [False] * n
    # 将每个点放入一个队列中，先进先出
    queue = deque([(xi, yi) for xi, yi in points if not visited])
    # 将队列按照方向反转，用于优化算法
    queue.reverse()
    # 用一个while循环遍历所有节点
    while queue:
        # 找到下一个要访问的节点
        next_xi = queue.popleft()
        # 如果这个节点已经访问过，说明无法到达最小值，返回已有最小值
        if next_xi in visited:
            return M
        # 标记这个节点已经访问过，防止重复访问
        visited[next_xi] = True
        # 如果当前节点距离起点很远，直接返回当前节点到起点的距离
        if M - abs(next_xi - xi) > n:
            return M - abs(next_xi - xi)
        # 枚举起点到当前节点的所有方向
        for i in range(n):
            next_x = xi + i
            # 如果当前节点到下一个节点的距离比当前节点到起点的距离小，说明有更优解
            if abs(next_x - xi) < abs(next_xi - xi - n):
                return min(M, find_min_days(M, n, points))
            # 否则继续沿着当前方向找到下一个节点
            next_y = yi + i
    return 0

result = find_min_days(M, n, points)
print(result)