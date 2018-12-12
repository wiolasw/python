#!/usr/bin/python

import random
from multiprocessing import Pool
import multiprocessing as mp
from multiprocessing import Process
from multiprocessing import Lock, Array


def createList(size):
    list = []
    for i in range(0, 100):
        list.append(random.randint(0, 39))
    return list


def createHistogram(size):
    list = [0] * 40
    return list


def hist(list, histogram, lk):
    for l in list:
        histogram[l] = histogram[l] + 1
    # return histogram


l = Lock()
pool = Pool(processes=2)
list = createList(100)
histogram = createHistogram(40)
hist(list, histogram, l)

arr = Array('i', range(40))
for k in range(0, 40):
    arr[k] = 0

p1 = Process(target=hist, args=(list[0:50], arr, l))
p2 = Process(target=hist, args=(list[50:100], arr, l))
p1.start()
p2.start()

p1.join()
p2.join()

for i in range(0, 40):
    print(arr[i] - histogram[i])

for i in range(0, 40):
    print(arr[i])
