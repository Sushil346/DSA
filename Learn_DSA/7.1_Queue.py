#!/usr/bin/env python
# coding: utf-8

import time
import threading


from collections import deque
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, val):
        self.buffer.appendleft(val)
    def deque(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)


def Place_Order(q, orders):
    for item in orders:
        q.enqueue(item)
        time.sleep(0.5)
        print(str(item) +"{ order is placed}")
    return q    
    
def Serve_Order(q):
    while q.size != 0:
        print(f"{q.deque()}, Served")
        time.sleep(2)
    return q    


orders = ['pizza','samosa','pasta','biryani','burger']
que = Queue()


thread_1 = threading.Thread(target=Place_Order, args=(que, orders,))
thread_2 = threading.Thread(target=Serve_Order, args=(que,))


thread_1.start()
time.sleep(1)
thread_2.start()




