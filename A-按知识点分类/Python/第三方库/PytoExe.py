''' 挑选工具 '''

from os import system,getcwd # ①命令行，②删除文件，③当前工作目录
from func.selDialog import Dialog # ①自定义模块，封装了win32ui.CreateFileDialog
from func.ending import del_file,del_folder,moveFile

''' 选择文件 '''

fileName, dirName, baseName, exeName = Dialog().openWindow("请选择py文件",'E:\Python3.11')

''' 处理文件 '''

goto = r"cd {}".format(dirName)
pyToexe = r"pyinstaller -F -w "+fileName
final_Command = goto + r" & " + pyToexe
system(final_Command)

    
''' 处理痕迹 '''

# 移动文件(查重路径，要移动的文件的路径，要移动到的目录，模式)
try:
    moveFile(exeName,dirName+r"\\dist\\"+baseName+"exe",dirName,'f') 
except:
    moveFile(exeName,dirName+r"dist"+baseName+"exe",dirName,'f') 

# 删除文件/文件夹(路径元组)
del_folder((dirName+"/dist",dirName+"/build"))
del_file(dirName+'/'+baseName+"spec")  
