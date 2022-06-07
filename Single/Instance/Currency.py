from Single.Basics.Main.Team import *


class Function():
    def __init__(self, window):
        self.window = window

    def multiplayerOfCaptain(self, times, numberOfPeople):
        # Main(self.window).checkIn()
        # Main(self.window).goInstanceList()
        # captain = InstanceList(self.window)
        # captain.selectInstance(instance, branch)
        # captain.createTeam()
        captain = Team(self.window)
        captain.inviteMember("invite2.png")
        if numberOfPeople == 3:
            captain.inviteMember("invite3.png")
        time.sleep(1)
        # captain.checkSetting()
        captain.captainGame(times, numberOfPeople)
        captain.backAfterGame()
        Explore(self.window).backTomain()

    def multiplayerOfMember(self, times):
        member = Team(self.window)
        member.acceptInvite()
        # member.checkSetting()
        member.memberGame(times)
        member.backAfterGame()
        Explore(self.window).backTomain()