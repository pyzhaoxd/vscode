from os import add_dll_directory
import tarfile


#打包xxx.tar.gz
tar_file = tarfile.open("work.tar.gz","w:gz")
for name in ["a.txt","b.txt"]:
    #tarfile.add_dll_directory(name)
    tar_file.add(name)
tar_file.close()



#查看
tar_file = tarfile.open("work.tar.gz","r:gz")
print(tar_file.getnames())