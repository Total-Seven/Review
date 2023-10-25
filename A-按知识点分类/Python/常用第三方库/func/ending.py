from os import system,remove,getcwd # ①命令行，②删除文件，③当前工作目录
from shutil import rmtree,move # ①遍历删除，②移动文件
from os.path import isfile

def moveFile(targetPath,oldPath,newDir,model):
    if model == 'f' and isfile(targetPath): # 检查目标文件是否已经存在,是则删除
        remove(targetPath)
    move(oldPath,newDir) # 移动目标文件到指定位置

def del_folder(paths):
    if isinstance(paths,(tuple,list)):
        for path in paths:
            rmtree(path)
    else:
        rmtree(paths)


def del_file(paths):
    if isinstance(paths,(tuple,list)):
        for path in paths:
            remove(path)
    else:
        remove(paths)