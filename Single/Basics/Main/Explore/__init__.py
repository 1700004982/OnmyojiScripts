from pyscreeze import Box

from Single.Basics import *

Explore_Path = "\\screenshot\\main\\explore\\"


class Explore():
    def __init__(self, window):
        self.loop = Loop(window)

    # 界面检测函数 直到底部探索列表出现 为成功进入界面

    def backTomain(self):
        time.sleep(1)
        self.loop.behavior.clickPosition(
            self.loop.behavior.getImageCompareResult(Explore_Path + "backtomain.png", Box(21, 53, 33, 33)))
