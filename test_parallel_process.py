# -*- coding: utf-8 -*-
from time import time
import subprocess

start = time()
procs = []

for i in range(10):
    proc = subprocess.Popen(['sleep',str(1)])
    procs.append(proc)

for proc in procs:
    proc.communicate()
    
end = time()
print("%f sec" %(end-start))