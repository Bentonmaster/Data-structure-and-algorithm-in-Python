from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    siqueue = Queue()
    for name in namelist:
        siqueue.enqueue(name)

    while siqueue.size() > 1:
        for i in range(num):
            siqueue.enqueue(siqueue.dequeue())

        siqueue.dequeue()
    return siqueue.dequeue()
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))