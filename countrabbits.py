#!/usr/bin/python

def rabbits(parent, offspring, k, n):
    if n > 40:
        print "n is not a valid number"
        return
    if k > 5:
        print "k is not a valid number"
        return
    month = 1
    pair = 1
    total = None
    while month <= n:
        if month == 1:
            total = 1
        else:
            total = rabbits(offspring, parent*k + offspring, k, n-1)
    else:
        print total

f = open("rosalind_fib.txt", 'r')
numbers = f.readlines()
input = numbers[0].split()
n = int(input[0])
k = int(input[1])

rabbits(0, 1, k, n)


