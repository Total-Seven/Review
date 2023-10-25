from os.path import basename, dirname  # ①文件存在，②去除上层目录
from win32ui import CreateFileDialog


class Dialog:
    def __init__(self):
        self.window = CreateFileDialog(bool('巴啦啦小魔仙~魔仙变！'))
        # dic["fileName"] = self.GetPathName()
        # TypeError: PyCFileDialog has read-only attributes
        # TypeError: __init__() should return None, not 'str'

    def openWindow(self, title, initialDir):
        self.window.SetOFNTitle(title)
        self.window.SetOFNInitialDir(initialDir)
        self.window.DoModal()

        fileName = self.window.GetPathName()
        dirName = dirname(fileName)
        baseName = basename(fileName).rstrip("py")
        exeName = fileName.rstrip("py")+"exe"

        return fileName, dirName, baseName, exeName
