class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if(len(self.__queue)>0):
            elem = self.__queue[0]
            del self.__queue[0]
            return elem
        else:
            raise QueueError

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
