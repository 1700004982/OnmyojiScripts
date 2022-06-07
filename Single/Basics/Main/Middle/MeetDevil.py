from pyscreeze import Box

from Single.Basics import *

Meet_Path = "\\screenshot\\main\\middle\\meetdevil\\"


class MeetDevil():
    def __init__(self, window):
        self.loop = Loop(window)

    # 界面检测函数 直到右下角鸟居出现 为成功进入界面

    def searchFourTimesGetAward(self):
        for num in range(1, 4):
            self.loop.behavior.clickPosition(Box(758, 435, 59, 52))
            time.sleep(2)
        self.loop.behavior.clickPosition(Box(822, 171, 30, 32))
        time.sleep(2)
        self.loop.behavior.clickPosition(Box(822, 171, 30, 32))

    def challengeBoss(self):
        self.loop.clickImageWhenFound(Meet_Path + "searchboss.png")
        self.loop.clickImageWhenFound(Meet_Path + "skeleton.png")
        self.loop.clickImageUntilDisappear(Meet_Path + "challenge.png")
        self.loop.clickImageUntilDisappear(Meet_Path + "ready.png")
        self.loop.clickImageUntilDisappear(Meet_Path + "win.png")

# 433 81
