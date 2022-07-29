import datetime
import os
from shutil import copyfile, copystat

s = datetime.datetime.now()
dir_name = str(s).replace(' ','_')
os.mkdir(dir_name)
os.chdir(dir_name)
for root, dirs, files in os.walk('/var/log'):
  for f in files:
    if 'log' in f:
      src = root + '/' + f
      copyfile(src, './' + f)
      copystat(src, './' + f)
