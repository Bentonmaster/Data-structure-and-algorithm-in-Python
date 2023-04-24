def digit_sum(x):
    # 计算一个数的各个数位之和
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

def count_reachable_cells(m, n, k):
    # 计算能到达的格子数量
    visited = [[False] * n for _ in range(m)]
    stack = [(0, 0)]
    count = 0
    while stack:
        i, j = stack.pop()
        if i < 0 or i >= m or j < 0 or j >= n:
            continue
        if visited[i][j]:
            continue
        if digit_sum(i) + digit_sum(j) > k:
            continue
        visited[i][j] = True
        count += 1
        stack.append((i-1, j))
        stack.append((i+1, j))
        stack.append((i, j-1))
        stack.append((i, j+1))
    return count

# 读取输入数据
m, n, k = map(int, input().split())

# 计算能到达的格子数量
count = count_reachable_cells(m, n, k)

# 输出结果
print(count)