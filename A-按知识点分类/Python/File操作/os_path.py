from os.path import abspath, dirname, basename, split
from os import getcwd
import sys

print(sys.argv[0])

print("-------------------")

cwd = getcwd()

print(cwd)
#  e:\1.007\Code Review\A-按知识点分类\Python\File操作

print(dirname(cwd))
#  e:\1.007\Code Review\A-按知识点分类\Python  (上一级)

print(basename(cwd))  # File操作             （文件名）(无后缀)

dirPath, FileName = split(cwd)
print(dirPath, FileName)
