from pyscreeze import Box

from Single.Basics import *

Team_Path = "\\screenshot\\main\\team\\"
Account_Path = "\\screenshot\\account\\"


class Team():
    def __init__(self, window):
        self.loop = Loop(window)

    # 界面检测函数 直到队长字出现 为成功进入界面

    def checkSetting(self):
        box = Box(15, 466, 29, 29)
        position = self.loop.behavior.getImageCompareResult(Team_Path + "lineuplockoff.png", box)
        if position is not None:
            self.loop.behavior.clickPosition(position)
        position = self.loop.behavior.getImageCompareResult(Team_Path + "autooff.png", box)
        if position is None:
            self.loop.behavior.clickPosition(position)

    def inviteMember(self, memberName):
        self.loop.clickImageInTime(Team_Path + "invite.png")
        self.loop.clickImageInTime(Account_Path + memberName)
        self.loop.clickImageInTime(Team_Path + "sendinvite.png")

    def acceptInvite(self):
        self.loop.clickImageWhenFound(Team_Path + "accept.png")

    def captainGame(self, times, numberOfPeople):
        if times == 0:
            times = 1
        time.sleep(2)
        wait = "member2zone.png"
        if numberOfPeople == 3:
            wait = "member3zone.png"
        self.loop.findImageCustomCondition(Team_Path + wait, condition="None")
        self.loop.clickImageUntilDisappear(Team_Path + "start.png")
        self.loop.clickImageUntilDisappear(Team_Path + "win.png")
        self.loop.clickImageUntilDisappear(Team_Path + "end.png")
        self.loop.clickImageWhenFound(Team_Path + "setofinvite.png")
        self.loop.clickImageInTime(Team_Path + "confirm.png")
        times = times - 1
        while times != 0:
            self.loop.findImageCustomCondition(Team_Path + wait, condition="None")
            self.loop.clickImageUntilDisappear(Team_Path + "start.png")
            self.loop.clickImageUntilDisappear(Team_Path + "win.png")
            self.loop.clickImageUntilDisappear(Team_Path + "end.png")
            times = times - 1
            print(times)

    def memberGame(self, times):
        if times == 0:
            times = 1
        self.loop.clickImageUntilDisappear(Team_Path + "win.png")
        self.loop.clickImageUntilDisappear(Team_Path + "end.png")
        self.loop.clickImageUntilDisappear(Team_Path + "autoaccept.png")
        times = times - 1
        while times != 0:
            self.loop.clickImageUntilDisappear(Team_Path + "win.png")
            self.loop.clickImageUntilDisappear(Team_Path + "end.png")
            times = times - 1

    def backAfterGame(self):
        time.sleep(1)
        self.loop.behavior.clickPosition(self.loop.behavior.getImagePosition(Team_Path + "back.png"))
        self.loop.clickImageUntilDisappear(Team_Path + "confirm.png")
