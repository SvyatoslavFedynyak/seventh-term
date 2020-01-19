import os, sys, time
from datetime import datetime
from lib import *

process = sys.argv[1]

work_file_path = get_work_file(process)
    
if process == 'date':
    interval = int(sys.argv[2])
    while True:
        write_date(work_file_path)
        print('Current time was written to {0}'.format(work_file_path), flush=True)
        time.sleep(interval)

if process == 'random':
    interval = int(sys.argv[2])
    min = int(sys.argv[3])
    max = int(sys.argv[4])
    while True:
        write_random(work_file_path, min, max)
        print('Random values (from {0} to {1}) was written to {2}'.format(min, max, work_file_path), flush=True)
        time.sleep(interval)

