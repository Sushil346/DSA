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
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
    def add_front(self):
        return 


def dec_to_bin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    
    return dec_to_bin(n//2) + str(n%2)

for i in range (1,11):
    print(dec_to_bin(i))
    time.sleep(1)


import time

def dec_to_bin(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    return dec_to_bin(n // 2) + str(n % 2) 

for i in range(1, 11):
    print(dec_to_bin(i))
    time.sleep(1)




