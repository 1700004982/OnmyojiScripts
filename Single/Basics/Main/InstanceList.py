from pyscreeze import Box

from Single.Basics import *

InstanceList_Path = "\\screenshot\\instancelist\\"


class InstanceList():
    # 界面数据初始化
    def __init__(self, window):
        self.loop = Loop(window)

    # 界面检测函数 等待左上角退出符号出现 为成功进入界面

    def selectInstance(self, instancePath, branchPath):
        time.sleep(1)
        self.loop.scrollToFind(InstanceList_Path + instancePath, Box(94, 114, 158, 365), -900)
        time.sleep(1)
        self.loop.scrollToFind(InstanceList_Path + branchPath, Box(297, 158, 70, 254), -800, 800)

    def createTeam(self):
        self.loop.clickImageWhenFound(InstanceList_Path + "create.png")
        self.loop.clickImageUntilDisappear(InstanceList_Path + "confirmcreate.png")