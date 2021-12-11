import shutil

#压缩
shutil.make_archive('work1','zip','work/')


#解压
shutil.unpack_archive('work1.zip')