import os
from posix import EX_CANTCREAT
import sys


print(sorted(os.listdir(sys.argv[1])))


#执行脚本
#python list_dir.py /root/etc 
