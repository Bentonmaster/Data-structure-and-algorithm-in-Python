from pythonds.basic.queue import Queue

import random

class Printer:
    # 打印机对象类
    def __init__(self, ppm):
        # 设置打印机的相关参数
        self.pagerate = ppm # 打印速度
        self.currentTask = None # 当前打印任务
        self.timeRemaining = 0 # 任务倒计时

    def trick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
        
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate # 60s = 1min 打印速度 = 页数 / 时间

class Task:
    # 打印任务类
    def __init__(self, time):
        self.timestamp = time # 任务创建时间
        self.pages = random.randrange(1, 21) # 任务页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
def newPrintTask():
    num = random.randrange(1, 181) # 1~180
    if num == 180:
        # 1/180的概率返回True,判断等于任何数都可以
        return True
    else:
        return False
    
# 将所需的三个类都定义好了，接下来就是模拟打印机的工作过程，进入程序的主体部分

def simulation(numSeconds, pagesPerMinute):
    # 模拟打印机的工作过程，numSeconds为模拟的时间，pagesPerMinute为打印机的打印速度
    labprinter = Printer(pagesPerMinute) # 创建打印机对象，设置打印速度
    printQueue = Queue() # 创建打印任务队列
    waitingtimes = [] # 等待时间列表

    for currentSecond in range(numSeconds):
        # 每秒钟都会进行一次判断，是否有新的打印任务,currentSecond为当前时间
        if newPrintTask():
            # 如果有新的打印任务，就创建一个任务对象，将其加入到打印任务队列中
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            # 如果打印机不忙，且打印任务队列不为空，就从打印任务队列中取出一个任务，交给打印机
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.trick()
        # 打印机每秒钟都会进行一次判断，是否有任务完成，如果有，就将打印机设置为空闲状态
        # 如果没有，就将打印机的倒计时减一

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))

for i in range(10):
    simulation(3600, 5)# 模拟1小时，打印速度为5页/分钟