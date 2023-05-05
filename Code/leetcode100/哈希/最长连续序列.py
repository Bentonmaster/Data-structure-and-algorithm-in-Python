def longestConsecutive(nums):
    # 创建一个空集合，用于快速查找数字是否存在
    num_set = set(nums)
    longest_streak = 0
    
    # 遍历数组中的每个数字
    for num in nums:
        # 如果当前数字的前一个数字不在集合中，即当前数字是一个序列的起点
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            # 继续查找当前数字的下一个数字，直到不再连续为止
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            # 更新最长序列的长度
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak
