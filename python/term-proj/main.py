import os
import sys
import subprocess
import threading

child = './child.py'
pipes = []

command = [sys.executable, child, 'date', '5']
pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
pipes.append(pipe)
command = [sys.executable, child, 'random', '1', '1', '100']
pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
pipes.append(pipe)


def create_and_poll(process, *args):    
    command = [sys.executable, child, process].extend(args)
    pipe = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    pipes.append(pipe)
    
    buffer = 'temp'

    while buffer:
        buffer = pipe.stdout.readline()
        print(buffer.decode('utf8'), end='')
        
threads = []

for pipe in pipes:
    work_thread = threading.Thread(target=create_and_poll, args=(pipe))
    threads.append(work_thread)
    work_thread.daemon = True

for thread in threads:
    thread.start()