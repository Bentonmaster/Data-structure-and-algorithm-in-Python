MOD = 10**9 + 7

def count_red(s):
    # 计算字符串 s 中 "red" 子序列的数量
    cnt = 0
    idx_r, idx_e, idx_d = -1, -1, -1
    for i in range(len(s)):
        if s[i] == 'r':
            idx_r = i
        elif s[i] == 'e' and idx_r != -1:
            idx_e = i
        elif s[i] == 'd' and idx_e != -1:
            idx_d = i
            cnt += 1
            idx_e = -1
            idx_r = -1
    return cnt

def calculate_weights(n):
    # 计算所有长度为 n 的字符串的权值之和
    weights = 0
    for i in range(3**n):
        s = ''
        x = i
        for j in range(n):
            s += 'red'[x % 3]
            x //= 3
        cnt = count_red(s)
        for j in range(1, n+1):
            weights = (weights + cnt * j) % MOD
            cnt //= 2
    return weights

n = int(input())
print(calculate_weights(n))