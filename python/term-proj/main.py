import os, sys
import subprocess

child = './child.py'
pipes = []

command = [sys.executable, child, 'date', '5']
pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
pipes.append(pipe)
command = [sys.executable, child, 'random', '1', '1', '100']
pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
pipes.append(pipe)

buffer = 'temp'

while buffer:
    for pipe in pipes:
        buffer = pipe.stdout.readline()
        print(buffer.decode('utf8'), end='')
  


