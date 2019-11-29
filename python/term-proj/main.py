import os, sys
import subprocess

range_start = 1
range_end = 3

childs = []
for child in range(range_start, range_end+1):
    childs.append('./child{0}.py'.format(child))

pipes = []
word  = 'connect'

for i in range(range_start, range_end+1):
  command = [sys.executable, childs[i]]
  
 
while pipes:
    pipe = pipes.pop()
    pipe.wait()

