from collections import deque

# 用于表示一个状态的类
class State:
    def __init__(self, x, y, t, d):
        self.x = x  # 当前位置的横坐标
        self.y = y  # 当前位置的纵坐标
        self.t = t  # 当前时间步
        self.d = d  # 前一个状态

# 用于表示一个位置的障碍物状态的类
class Obstacle:
    def __init__(self, states):
        self.states = states  # 一个长度为 3 的布尔型列表，表示每个时间步的状态

# 将一个状态转化为字符串，方便放入集合中去重
def state_to_str(state):
    return f"{state.x},{state.y},{state.t},{state.d}"

# 将字符串转化为状态
def str_to_state(s):
    x, y, t, d = map(int, s.split(","))
    return State(x, y, t, d)

# 判断当前位置的障碍物状态是否为 1，需要考虑循环
def is_obstacle(obstacle, t):
    return obstacle.states[t % 3]

# 判断是否可以向该方向扩散
def can_expand(x, y, t, d, dx, dy, obstacles, n):
    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= n:
        # 超出地图边界，不能扩散
        return False
    if is_obstacle(obstacles[x+dx][y+dy], (t+1)%3):
        # 下一个时间步该位置存在障碍物，不能扩散
        return False
    if d is not None and dx == -d.x and dy == -d.y:
        # 和上一个状态相反的方向，不能扩散
        return False
    return True

# 扩散到下一个状态
def expand(state, dx, dy, obstacles, n):
    x, y, t, _ = state.x, state.y, state.t, state.d
    if can_expand(x, y, t, state.d, dx, dy, obstacles, n):
        return State(x + dx, y + dy, t + 1, state)
    else:
        return None

# 广度优先搜索
def bfs(start, end, obstacles, n):
    visited = set()  # 记录访问过的状态
    queue = deque([start])
    visited.add(state_to_str(start))
    while queue:
        cur = queue.popleft()
        if cur.x == end.x and cur.y == end.y:
            # 找到终点，回溯到起点，记录每个状态的时间
            path = []
            while cur is not None:
                path.append(cur.t)
                cur = cur.d
            return path[-1]
        # 尝试向四个方向扩散
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_state = expand(cur, dx, dy, obstacles, n)
            if next_state is not None and state_to_str(next_state) not in visited:
                visited.add(state_to_str(next_state))
                queue.append(next_state)
   
