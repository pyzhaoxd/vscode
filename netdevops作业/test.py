



# import sys
# print(sys.platform)

# print('\n'.join(dir(sys)))


# addaudithook
# api_version
# argv
# audit
# base_exec_prefix
# base_prefix
# breakpointhook
# builtin_module_names
# byteorder
# call_tracing
# copyright
# displayhook
# dllhandle
# dont_write_bytecode
# exc_info
# excepthook
# exec_prefix
# executable
# exit
# flags
# float_info
# float_repr_style
# get_asyncgen_hooks
# get_coroutine_origin_tracking_depth
# getallocatedblocks
# getdefaultencoding
# getfilesystemencodeerrors
# getfilesystemencoding
# getprofile
# getrecursionlimit
# getrefcount
# getsizeof
# getswitchinterval
# gettrace
# getwindowsversion
# hash_info
# hexversion
# implementation
# int_info
# intern
# is_finalizing
# maxsize
# maxunicode
# meta_path
# modules
# path
# path_hooks
# path_importer_cache
# platform
# platlibdir
# prefix
# pycache_prefix
# set_asyncgen_hooks
# set_coroutine_origin_tracking_depth
# setprofile
# setrecursionlimit
# setswitchinterval
# settrace
# stderr
# stdin
# stdout
# thread_info
# unraisablehook
# version
# version_info
# warnoptions
# winver

# import sys
# sys.stdout = open('test.txt','w')
# print ('Hello world')


# import sys
# temp = sys.stdout
# sys.stdout = open('test.txt','w')
# print ('hello world')
# sys.stdout = temp #恢复默认映射关系
# print ('nice')

# import sys
# print(sys.getdefaultencoding())
# print('/n'.join(sys.path[0]))

import sys
# l = sys.stdin.readline()
# print(l)


import sys
 
sys.stdout = open('Output.txt',mode='w')
sys.stderr = open('Stderr.txt',mode='w')
 
sample_input = ['Hi', 'Hello from AskPython', 'exit']
 
for ip in sample_input:
    # Prints to stdout
    sys.stdout.write(ip + '\n')
    # Tries to add an Integer with string. Raises an exception
    try:
        ip = ip + 100
    # Catch all exceptions
    except:
        sys.stderr.write('Exception Occurred!\n')