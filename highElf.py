from tkinter import *
from highElfFunctions import *
import random

def updateOptions(*args):
    mainSelection = mainChoice.get()
    subCurrentOptions = subOptions[mainSelection]

    secondMenu['menu'].delete(0, 'end')
    for option in subCurrentOptions:
        secondMenu['menu'].add_command(label=option, command=lambda opt=option:secondChoice.set(opt))
    secondChoice.set(subCurrentOptions[0])
    thirdMenu['menu'].delete(0, 'end')
    for option in subCurrentOptions:
        thirdMenu['menu'].add_command(label=option, command=lambda opt=option: thirdChoice.set(opt))
    thirdChoice.set(subCurrentOptions[0])
    fourthMenu['menu'].delete(0, 'end')
    for option in subCurrentOptions:
        fourthMenu['menu'].add_command(label=option, command=lambda opt=option: fourthChoice.set(opt))
    fourthChoice.set(subCurrentOptions[0])

def output():
    global text
    textContent = "你的军队：\n"
    mapTextContent = "地图："
    Choices = [[mainChoice.get(), mainLevelChoice.get()],
               [secondChoice.get(), secondLevelChoice.get()],
               [thirdChoice.get(), thirdLevelChoice.get()],
               [fourthChoice.get(), fourthLevelChoice.get()]]
    for choice in Choices:
        if choice[0] == '民兵团':
            textContent += militiaChooser(choice[1])
        elif choice[0] == '正规军':
            textContent += regularArmyChooser(choice[1])
        elif choice[0] == '洛瑟恩海卫团':
            textContent += roserenGuardChooser(choice[1])
        elif choice[0] == '查瑞斯禁卫团':
            textContent += charesGuardChooser(choice[1])
        elif choice[0] == '艾里昂掠夺者团':
            textContent += alyonRaiderChooser(choice[1])
        elif choice[0] == '荷斯白塔军':
            textContent += herseChooser(choice[1])
        elif choice[0] == '鹰爪弩炮团':
            textContent += eagleClawCrossbowChooeser(choice[1])
        elif choice[0] == '影子军团':
            textContent += shadowArmyChooser(choice[1])
        elif choice[0] == '银盔骑士团':
            textContent += silverHelmKnightChooser(choice[1])

    if mainChoice == '荷斯白塔军':
        mapTextContent = "荷斯之塔"

    text.set(textContent)
    mapText.set(mapTextContent)

root = Tk()
root.geometry("800x450+100+200")

mainOptions = ['民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '荷斯白塔军', '影子军团', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团']
subOptions = {
    '民兵团': ['无', '民兵团', '艾里昂掠夺者团', '鹰爪弩炮团'],
    '正规军': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '洛瑟恩海卫团': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '查瑞斯禁卫团': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '荷斯白塔军': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '荷斯白塔军', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '影子军团': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '荷斯白塔军', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '艾里昂掠夺者团': ['无', '民兵团', '艾里昂掠夺者团', '鹰爪弩炮团'],
    '银盔骑士团': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '荷斯白塔军', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '银战车团': ['无', '民兵团', '正规军', '洛瑟恩海卫团', '查瑞斯禁卫团', '影子军团', '荷斯白塔军', '艾里昂掠夺者团', '银盔骑士团', '银战车团', '鹰爪弩炮团'],
    '鹰爪弩炮团': ['无', '民兵团', '艾里昂掠夺者团', '鹰爪弩炮团'],
}
levelOptions = ['初入战场', '经验丰富', '久战沙场']

mainLabel = Label(root, text="选择你的领主军团：")
mainLabel.place(x=0, y=0)
mainChoice = StringVar()
mainMenu = OptionMenu(root, mainChoice, *mainOptions, command = updateOptions)
mainChoice.set(mainOptions[0])
mainMenu.place(x=150, y=0)
mainLevelChoice = StringVar()
mainLevelMenu = OptionMenu(root, mainLevelChoice, *levelOptions)
mainLevelChoice.set(levelOptions[0])
mainLevelMenu.place(x=300, y=0)

secondLabel = Label(root, text="选择你的第二个军团：")
secondLabel.place(x=0, y=30)
secondChoice = StringVar()
secondMenu = OptionMenu(root, secondChoice, '')
secondMenu.place(x=150, y=30)
secondLevelChoice = StringVar()
secondLevelMenu = OptionMenu(root, secondLevelChoice, *levelOptions)
secondLevelChoice.set(levelOptions[0])
secondLevelMenu.place(x=300, y=30)

thirdLabel = Label(root, text="选择你的第三个军团：")
thirdLabel.place(x=0, y=60)
thirdChoice = StringVar()
thirdMenu = OptionMenu(root, thirdChoice, '')
thirdMenu.place(x=150, y=60)
thirdLevelChoice = StringVar()
thirdLevelMenu = OptionMenu(root, thirdLevelChoice, *levelOptions)
thirdLevelChoice.set(levelOptions[0])
thirdLevelMenu.place(x=300, y=60)

fourthLabel = Label(root, text="选择你的第四个军团：")
fourthLabel.place(x=0, y=90)
fourthChoice = StringVar()
fourthMenu = OptionMenu(root, fourthChoice, '')
fourthMenu.place(x=150, y=90)
fourthLevelChoice = StringVar()
fourthLevelMenu = OptionMenu(root, fourthLevelChoice, *levelOptions)
fourthLevelChoice.set(levelOptions[0])
fourthLevelMenu.place(x=300, y=90)

button = Button(root, text="确认", command=output)
button.place(x=0, y=125)

text = StringVar()
label = Label(root, textvariable=text, justify=LEFT, wraplength=780)
label.place(x=0, y=175)

mapText = StringVar()
mapLabel = Label(root, textvariable=mapText, justify=LEFT)
mapLabel.place(x=0, y=275)

updateOptions()
root.mainloop()