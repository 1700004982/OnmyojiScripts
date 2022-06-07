import random
import time
import pyautogui


class Behavior():
    # 初始化
    def __init__(self, window):
        self.x = window.left
        self.y = window.top
        self.width = window.width
        self.height = window.height

    # 寻找图像在窗口内位置
    def getImagePosition(self, imagePath, accuracy=0.9):
        return pyautogui.locate(imagePath, pyautogui.screenshot(region=(self.x, self.y, self.width, self.height)),
                                confidence=accuracy)

    def getImageCompareResult(self, imagePath, box, accuracy=0.9):
        return pyautogui.locate(imagePath, pyautogui.screenshot(region=(self.x + box.left, self.y + box.top, box.width, box.height)),
                                confidence=accuracy)

    # 点击位置坐标
    def clickPosition(self, position, clicks=1, duration=0.2, accuracy=0.9):
        if position is not None:
            x, y = pyautogui.center(position)
            offsetWidth, offsetHeight = round(random.uniform(-1, 1) * position.width / 2, 4), round(
                random.uniform(-1, 1) * position.height / 2, 4)
            pyautogui.click(x + offsetWidth + self.x, y + offsetHeight + self.y, clicks, random.uniform(0.1, 1))
        else:
            return False

    # 区域内滚动
    def scrollInRegion(self, clicks, coordinate):
        if coordinate is not None:
            x, y = pyautogui.center(coordinate)
            offsetWidth, offsetHeight = round(random.uniform(-1, 1) * coordinate.width / 2, 4), round(
                random.uniform(-1, 1) * coordinate.height / 2, 4)
            pyautogui.moveTo(x + offsetWidth + self.x, y + offsetHeight + self.y)
            pyautogui.scroll(clicks, x + offsetWidth + self.x, y + offsetHeight + self.y)
        else:
            return False

    # 测试用截图
    def screenshotToSave(self, Box):
        pyautogui.screenshot("D:\\Project\\Python\\OnmyojiScripts\\screenshot\\Temp.png", region=Box)


class Loop():
    def __init__(self, window):
        self.behavior = Behavior(window)

    # 持续监控
    # 前置阻塞 上一步未完成则不进行操作
    def clickImageWhenFound(self, imagePath):
        position = None
        while position is None:
            position = self.behavior.getImagePosition(imagePath)
            time.sleep(random.uniform(0.5, 1))
        self.behavior.clickPosition(position)

    # 前置中置阻塞 上一步未完成不进行操作 当前操作未完成不停止操作
    def clickImageUntilDisappear(self, imagePath):
        self.clickImageWhenFound(imagePath)
        position = self.behavior.getImagePosition(imagePath)
        while position is not None:
            self.behavior.clickPosition(position)
            position = self.behavior.getImagePosition(imagePath)
            time.sleep(random.uniform(0.5, 1))

    # 前置后置阻塞 上一步未完成不进行操作 下一步开始前不停止操作
    def clickImageUntilAppearNext(self, imagePath, nextPath):
        self.clickImageWhenFound(imagePath)
        nextPosition = self.behavior.getImagePosition(nextPath)
        while nextPosition is None:
            self.behavior.clickPosition(self.behavior.getImagePosition(imagePath))
            nextPosition = self.behavior.getImagePosition(nextPath)
            time.sleep(random.uniform(0.5, 1))

    # 自定义阻塞 当该图片状态满足条件时 结束阻塞
    def findImageCustomCondition(self, imagePath, condition):
        position = self.behavior.getImagePosition(imagePath)
        if condition == "None":
            while position is not None:
                position = self.behavior.getImagePosition(imagePath)
                time.sleep(random.uniform(0.5, 1))
        elif condition == "not None":
            while position is None:
                position = self.behavior.getImagePosition(imagePath)
                time.sleep(random.uniform(0.5, 1))

    # 超时后停止监控
    def clickImageInTime(self, imagePath, times=5):
        for times in range(0, times):
            position = self.behavior.getImagePosition(imagePath)
            if position is not None:
                self.behavior.clickPosition(position)
                return True
            time.sleep(0.5)

    # 持续滚动查找某个控件
    def scrollToFind(self, imagePath, scrollRegion, scrollSize, topDistance=2000):
        self.behavior.scrollInRegion(topDistance, scrollRegion)
        while self.behavior.getImagePosition(imagePath) is None:
            self.behavior.scrollInRegion(scrollSize, scrollRegion)
            time.sleep(random.uniform(0.5, 1))
        self.behavior.clickPosition(self.behavior.getImagePosition(imagePath))
