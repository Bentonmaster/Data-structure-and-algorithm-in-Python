# 定义特殊字符的加法规则
special_addition = {
    "!+!": 0,
    "!+@": 13,
    "!+#": 4,
    "@+@": 7,
    "@+#": 20,
    "#+#": 5
}

# 从标准输入中读取表达式
n = int(input())
expression = input()

# 判断表达式中是否包含特殊字符
has_special_char = ("!" in expression) or ("@" in expression) or ("#" in expression)

if has_special_char:
    # 处理特殊字符的加法
    for special in special_addition:
        if special in expression:
            expression = expression.replace(special, str(special_addition[special]))

# 将表达式按照运算符分割成左右两个操作数
left_operand, right_operand = expression.split("+")

# 将操作数转换成浮点数进行计算
result = float(left_operand) + float(right_operand)

# 将计算结果转换成字符串形式，去掉末尾的0
result_str = str(result).rstrip("0").rstrip(".")

# 输出计算结果
print(result_str)
