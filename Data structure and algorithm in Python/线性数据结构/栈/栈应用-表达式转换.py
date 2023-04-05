# 中缀表达式转后缀表达式
from pythonds.basic.stack import Stack

def infixToPostfix(infixexpr):
    # 用字典来操作符的优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    # 创建一个空栈opstack用于暂存操作符
    opstack = Stack()
    # 创建一个空列表postfixList用于存储后缀表达式
    postfixList = []
    # 用空格分隔表达式中的各个元素
    tokenList = infixexpr.split()
    # 遍历tokenList中的元素
    for token in tokenList:
        # 如果是操作数,则直接添加到postfixList中
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        # 如果是左括号,则直接压入opstack
        elif token == '(':
            opstack.push(token)
        # 如果是右括号,则弹出opstack中的元素,直到遇到左括号
        elif token == ')':
            tokenout = opstack.pop()
            while tokenout != '(':
                postfixList.append(tokenout)
                tokenout = opstack.pop()
        # 如果是操作符,则比较其与opstack栈顶元素的优先级,
        # 如果优先级高,则压入opstack,否则弹出opstack中的元素,直到遇到优先级低的元素
        # 最后将当前操作符压入opstack，如果opstack为空，则直接压入
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    # 如果opstack不为空,则将其中的剩余的元素依次弹出,添加到postfixList中
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())
    # 返回后缀表达式
    return " ".join(postfixList)
