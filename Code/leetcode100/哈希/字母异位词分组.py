from collections import defaultdict
from typing import List

def groupAnagrams(strs):
    # 创建一个 defaultdict，值的默认类型为列表
    groups = defaultdict(list)
    
    for word in strs:
        # 将单词按字母顺序排序，得到排序后的新单词
        sorted_word = ''.join(sorted(word))
        
        # 将当前单词添加到对应的字母异位词组中
        groups[sorted_word].append(word)
    
    # 将字母异位词组的值转换为列表并返回
    return list(groups.values())


# 官方解法
# 普通列表

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            s_ = "".join(sorted(s))
            if s_ not in dic:
                dic[s_] = [s]
            else:
                dic[s_].append(s)
        return list(dic.values())
