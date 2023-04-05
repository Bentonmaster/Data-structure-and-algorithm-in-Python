# 变位词问题：两个字符串中的字符相同，但是顺序不同
# 解法1：逐字检测
def anagramSlution1(s1,s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 <len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 +1
        if found:
            alist[pos2] = None
        else:
            stillOK = False
        pos1 = pos1 +1
    return stillOK

# 解法2：排序后比较
def anagramSlution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

# 解法3：暴力法 增长速度过大n！大于2^n，不可取

# 解法4：计数比较
def anagramSlution4(s1,s2):
    #计数器
    c1 = [0]*26
    c2 = [0]*26
    #分别计数
    for i in range(len(s1)):
        # ord()函数返回对应字符的ASCII数值
        # 通过减去a的ASCII数值，得到该字母在字母表中的位置，返回一个整数
        # 若改为用字典作为计数器，可避免这一步
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            stillOK = False
    return stillOK