# 定义一个函数来计算后缀表达式
def suffix_exp_calculate(suffix_exp):
    # 创建空栈用于暂存操作数
    stack = []
    # 将后缀表达式用split()函数分割成列表
    suffix_exp = suffix_exp.split()
    # 遍历列表中的每个元素
    for i in suffix_exp:
        # 如果单词为操作数，将其转换为整数int，然后压入栈中
        if i.isdigit():
            stack.append(int(i))
        # 如果单词为操作符，将栈顶的两个元素弹出，然后进行运算，将运算结果压入栈中
        else:
            # 弹出栈顶的两个元素
            num2 = stack.pop()
            num1 = stack.pop()
            # 使用一个domath函数进行运算
            result = domath(i, num1, num2)
            # 将运算结果压入栈中
            stack.append(result)
    # 返回栈中的最后一个元素
    return stack.pop()

# 定义一个函数来进行运算
def domath(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    else:
        return "Error"

# 测试
print(suffix_exp_calculate("4 5 6 * +"))
print(suffix_exp_calculate("7 8 + 3 2 + /"))

