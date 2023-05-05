def jump(nums):
    n = len(nums)
    if n == 1:
        return 0
    
    jumps = 0  # 记录跳跃次数
    cur_end = 0  # 当前可达到的最远位置
    cur_max = 0  # 当前位置能够到达的最远位置
    
    for i in range(n - 1):
        cur_max = max(cur_max, i + nums[i])  # 更新当前位置能够到达的最远位置
        
        if i == cur_end:  # 遍历到当前可达到的最远位置
            jumps += 1
            cur_end = cur_max
        
        if cur_end >= n - 1:  # 如果已经到达终点
            return jumps
    
    return jumps
