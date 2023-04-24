import operator
from pythonds.basic.stack import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            return ValueError
    return eTree

def evaluate(paresTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = paresTree.getLeftChild()
    rightC = paresTree.getRightChild()

    if leftC and rightC:
        fn = opers[paresTree.getRootVal()]
        
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        print(paresTree.getRootVal())
        return paresTree.getRootVal()

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
        
# 采用中序遍历的方式，将表达式树转换为普通的表达式
# 对叶节点进行特殊处理
def printexp(tree):
    sVal = ""
    if tree:
        if tree.getLeftChild() is not None:
            sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        if tree.getRightChild() is not None:
            sVal = sVal + printexp(tree.getRightChild())+')'
    return sVal


fpexp = '( 3 * ( 5 + 1 ) )'
eTree = buildParseTree(fpexp)
print(printexp(eTree))
print(evaluate(eTree))