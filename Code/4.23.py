from collections import deque

from collections import deque

def find_min_days(M, n, points):
    grass = {}
    for x, y in points:
        if (x, y) not in grass:
            grass[(x, y)] = 1
        else:
            grass[(x, y)] += 1
    
    queue = deque([(x, y) for x, y in grass.keys()])
    days =0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in grass:
                    grass[(nx, ny)] = 1
                    queue.append((nx, ny))
                else:
                    grass[(nx, ny)] += 1
                if grass[(nx, ny)] >= M:
                    return days + 1
        days += 1
    return 0


# 从标准输入中读取输入数据
M = int(input())
n = int(input())
points = []
for _ in range(n):
    xi, yi = map(int, input().split())
    points.append([xi, yi])

# 调用函数得到输出结果
result = find_min_days(M, n, points)

# 将输出结果打印到标准输出中
print(result)