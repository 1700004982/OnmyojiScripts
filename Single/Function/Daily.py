import threading

from Single.Instance.Currency import *

window1 = Box(0, 0, 868, 520)
window2 = Box(867, 0, 868, 520)


def captainTh():
    Function(window1).multiplayerOfCaptain(600, 2)


def member1Th():
    Function(window2).multiplayerOfMember(600)


T1 = threading.Thread(target=captainTh)
T2 = threading.Thread(target=member1Th)
T1.start()
T2.start()
