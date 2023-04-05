# list.pop的计时实验
# import timeit
# popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
# popend = timeit.Timer('x.pop()', 'from __main__ import x')
# print("pop(0)   pop()")

# 通过改变列表大小来测试两个操作的增长趋势
# 从1000000到100000000，步长为1000000
# for i in range (1000000, 100000001, 1000000):
#     x = list(range(i))
#     pt = popend.timeit(number=1000)
#     x = list(range(i))
#     pz = popzero.timeit(number=1000)
#     print("%15.5f, %15.5f" % (pz, pt))

# list和dict的in操作的计时实验
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, 
                     "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d, %10.3f, %10.3f" % (i, lst_time, d_time))