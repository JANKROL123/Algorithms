import sys
import math
from timeit import default_timer as timer
import random
import threading
sys.setrecursionlimit(2**15)
threading.stack_size(2**21)
def quickSort(A):
    p = 0
    r = len(A) - 1
    def partition(A, p, r):
        rnd = random.randint(p, r)
        x = A[rnd]
        A[rnd], A[r] = A[r], A[rnd]
        i = p - 1
        for j in range(p, r + 1):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        if i < r:
            return i
        else:
            return i - 1
    def auxiliary_function(A, p, r):
        if p < r:
            q = partition(A, p, r)
            auxiliary_function(A, p, q)
            auxiliary_function(A, q + 1, r)
        return A
    y = auxiliary_function(A, p, r)
    return y
c = 8
def quickSort_modified(A):
    p = 0
    r = len(A) - 1
    def partition(A, p, r):
        rnd = random.randint(p, r)
        x = A[rnd]
        A[rnd], A[r] = A[r], A[rnd]
        i = p - 1
        for j in range(p, r + 1):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        if i < r:
            return i
        else:
            return i - 1
    def auxiliary_function_modified(A, p, r):
        if p < r:
            if len(A[p:r + 1]) < c:
                for a in range(r, p, -1):
                    for b in range(p, a):
                        if A[b] > A[b + 1]:
                            A[b], A[b + 1] = A[b + 1], A[b]
            else:
                q = partition(A, p, r)
                auxiliary_function_modified(A, p, q)
                auxiliary_function_modified(A, q + 1, r)
        return A
    y = auxiliary_function_modified(A, p, r)
    return y

