import glob

#当前路径查找所有txt文件
file_math = glob.glob('*.txt')
print(file_math)


file_math = glob.glob('[0-9].txt')
print(file_math)

#返回文件和所在的目录
file_math = glob.glob('**/*.txt',recursive=True)
print(file_math)

#只返回文件所在的目录
file_math = glob.glob('**/.txt',recursive=True)
print(file_math)
