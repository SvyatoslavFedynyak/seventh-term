import os, sys, time
from datetime import datetime
from lib import *

process = sys.argv[0]

work_file_path = get_work_file(process)
    
if process == 'date':
    write_date(process, sys.argv[2])

