# 导入list
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result
                else:
                    continue


# 官方解法
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)  # 获取输入列表 nums 的长度
        h = {}  # 创建一个空的字典用于存储元素和对应的索引
        for i, v in enumerate(nums):  # 遍历输入列表 nums，同时获取元素和对应的索引
            j = h.get(target - v, None)  # 在字典中查找是否存在满足条件的元素
            if j is not None:  # 如果找到满足条件的元素
                return [i, j]  # 返回满足条件的元素的索引
            h[v] = i  # h[v] = i 将当前元素 v 作为字典的键，将对应的索引 i 作为值，将它们存储到字典 h 中

# enumerate() 是一个内置函数，用于遍历可迭代对象（如列表、字符串等）并同时获取元素的索引和值。
# h.get(key, default) 是字典的一个方法，用于获取字典中键为 key 的值。如果键存在，则返回对应的值；如果键不存在，则返回默认值 default。