from tkinter import *
import random
from functions0 import *

currentFrame = None
ownArmy = ""
enemyArmy = ""

root = Tk()
root.geometry("800x450+100+200")

startPage = Frame(root)
currentFrame = startPage
startPage.grid()
introLabel = Label(startPage, text="选择你的种族")
introLabel.grid()
def introEmpire():
    global currentFrame
    currentFrame.grid_forget()
    empirePage.grid()
    currentFrame=empirePage
introEmpireButton = Button(startPage, text="帝国", command=introEmpire)
introEmpireButton.grid(row=1)

empirePage = Frame(root)
empireLabel = Label(empirePage, text="你的身份是？")
empireLabel.grid()
def empireGeneral():
    global ownArmy, currentFrame
    currentFrame.grid_forget()
    empireGeneralPage.grid()
    currentFrame = empireGeneralPage
    #开始随机组建军队
    ownArmy += "你的军队：帝国将军（），剑士（），剑士（），长戟兵（），弩手（），帝国队长（战马），先驱侍骑（），先驱侍骑（），帝国骑士（），帝国骑士（）"
    ownArmy = mediumEmpireGeneralChooser(ownArmy)
    ownArmy = mediumEmpireCaptainChooser(ownArmy)
    ownArmy = levelChooser(ownArmy, "剑士", 7, 9)
    ownArmy = levelChooser(ownArmy, "剑士", 7, 9)
    ownArmy = levelChooser(ownArmy, "长戟兵", 4, 6)
    ownArmy = levelChooser(ownArmy, "弩手", 7, 9)
    ownArmy = levelChooser(ownArmy, "先驱侍骑", 3, 4)
    ownArmy = levelChooser(ownArmy, "先驱侍骑", 3, 4)
    ownArmy = levelChooser(ownArmy, "帝国骑士", 2, 3)
    ownArmy = levelChooser(ownArmy, "帝国骑士", 2, 3)
empireGeneralButton = Button(empirePage, text="将军", command=empireGeneral)
empireGeneralButton.grid(row=1)

empireGeneralPage = Frame(root)
empireGeneralLabel = Label(empireGeneralPage, text="你准备前往哪里")
empireGeneralLabel.grid()
def empireGeneralDemestic():
    global enemyArmy, currentFrame
    currentFrame.grid_forget()
    empireGeneralDomesticPage.grid()
    currentFrame = empireGeneralDomesticPage
    #开始随机抽取事件
    empireGeneralDomesticEvent = random.choices(list(empireGeneralDomesticDict.keys()),
                                                weights=list(empireGeneralDomesticDict.values()), k=1)[0]
    if empireGeneralDomesticEvent == "镇压瑞克领叛军":
        #开始随机组建叛军部队
        enemyArmy += "敌人军队：帝国队长（）+长矛兵（）+帝国弓箭手（）+自由民兵团（）+自由民兵团（）"
        enemyArmy = mediumEmpireCaptainChooser(enemyArmy)
        enemyArmy = levelChooser(enemyArmy, "长矛兵", 1, 3)
        enemyArmy = levelChooser(enemyArmy, "帝国弓箭手", 1, 3)
        enemyArmy = levelChooser(enemyArmy, "自由民兵团", 1, 3)
        enemyArmy = levelChooser(enemyArmy, "自由民兵团", 1, 3)
        empireGeneralDomesticLabel.config(text="你在瑞克领遇到了小规模叛军\n" + ownArmy+"\n"+enemyArmy+"\n地图：瑞克领宅地")
    elif empireGeneralDomesticEvent == "镇压米登领叛军":
        enemyArmy += "敌人军队：猎人将军（）+自由民兵团（）+长矛兵（）+猎人（）+猎人（）"
        enemyArmy = mediumEmpireHunterChooser(enemyArmy)
        enemyArmy = levelChooser(enemyArmy, "长矛兵", 1, 3)
        enemyArmy = levelChooser(enemyArmy, "自由民兵团", 1, 3)
        enemyArmy = levelChooser(enemyArmy, "猎人", 1, 4)
        enemyArmy = levelChooser(enemyArmy, "猎人", 1, 4)
        empireGeneralDomesticLabel.config(text="你在米登领遇到了小规模叛军\n" + ownArmy + "\n" + enemyArmy+"\n地图：魔女林")
    elif empireGeneralDomesticEvent == "镇压威森领叛军":
        enemyArmy += "敌人军队：帝国队长（）+自由民兵团（）+自由民兵团（）+火枪手（）+臼炮（）"
        enemyArmy = mediumEmpireCaptainChooser(enemyArmy)
        enemyArmy = levelChooser(enemyArmy, "自由民兵团", 2, 4)
        enemyArmy = levelChooser(enemyArmy, "自由民兵团", 2, 4)
        enemyArmy = levelChooser(enemyArmy, "火枪手", 2, 4)
        enemyArmy = levelChooser(enemyArmy, "臼炮", 2, 4)
        empireGeneralDomesticLabel.config(
            text="你在威森领遇到了小规模叛军\n" + ownArmy + "\n" + enemyArmy + "\n地图：铁矿")
empireGeneralDemesticButton = Button(empireGeneralPage, text="帝国境内", command=empireGeneralDemestic)
empireGeneralDemesticButton.grid(row=1)

empireGeneralDomesticPage = Frame(root)
empireGeneralDomesticDict = {"镇压瑞克领叛军":1, "镇压米登领叛军":1, "镇压威森领叛军":1}
empireGeneralDomesticLabel = Label(empireGeneralDomesticPage, wraplength=800, justify=LEFT)
empireGeneralDomesticLabel.grid()

root.mainloop()