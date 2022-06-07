from Single.Basics import *


# 全局观察类 寻找会影响进程的特殊事件
class SpecialEvents():
    def overallSituation(self):
        screenshot = pyautogui.screenshot("D:\\Project\\Python\\OnmyojiScripts\\screenshot\\Temp.png",
                                          region=(0, 0, 1736, 1040))
        # 御魂达到6000上限
        if pyautogui.locate(Events_Path + "soulfull.png", screenshot) is not None:
            position = pyautogui.locate(Events_Path + "soulfull.png", screenshot)
            x, y = position.left, position.top
            pyautogui.click(random.uniform(0.1, 1))
    # 第一次登陆绑定手机

    # 第一次逢魔锁定boss
