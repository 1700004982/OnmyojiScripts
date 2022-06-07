from Single.Basics import *

Middle_Path = "\\screenshot\\main\\middle\\"


class Middle():
    def __init__(self, window):
        self.loop = Loop(window)

    # 界面检测函数 直到左上角退出符出现 为成功进入界面 该符号并不唯一 待定

    def goMeetDevil(self):
        self.loop.clickImageWhenFound(Middle_Path + "meetdevil.png")
