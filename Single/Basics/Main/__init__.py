# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from pyscreeze import Box

from Single.Basics import *

Main_Path = "\\screenshot\\main\\"


class Main():
    def __init__(self, window):
        self.loop = Loop(window)

    # 页面检测方法 一直点击总控件 直到检测到总控件出现 为成功进入界面
    def checkIn(self):
        position = self.loop.behavior.getImagePosition(Main_Path + "bar.png")
        while position is None:
            self.loop.behavior.clickPosition(Box(800, 413, 44, 92))
            position = self.loop.behavior.getImagePosition(Main_Path + "bar.png")
            time.sleep(random.uniform(0.5, 1))

    def goMiddle(self):
        self.loop.clickImageUntilDisappear(Main_Path + "middle.png")

    def goInstanceList(self):
        self.loop.clickImageUntilDisappear(Main_Path + "team.png")


