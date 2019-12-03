import os
import sys
import subprocess
import threading

child = './child.py'

def create_and_poll(process, *args):    
    command = [sys.executable, child, process]
    command.extend(args)
    pipe = subprocess.Popen(command, stdout=subprocess.PIPE)
    
    buffer = 'temp'

    while buffer:
        buffer = pipe.stdout.readline()
        print(buffer.decode('utf8'), end='')
        
threads = []

work_thread = threading.Thread(target=create_and_poll, args=['date', '3'])
threads.append(work_thread)
work_thread = threading.Thread(target=create_and_poll, args=['random', '1', '1', '100',])
threads.append(work_thread)

for thread in threads:
    thread.start()