from tkinter import *
from kislevFunctions import *
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
        if choice[0] == '哥萨民兵团':
            textContent += gosaMilitiaChooser(choice[1])
        elif choice[0] == '哥萨正规军':
            textContent += gosaRegularArmyChooser(choice[1])

    text.set(textContent)
    mapText.set(mapTextContent)

root = Tk()
root.geometry("800x450+100+200")

mainOptions = ['哥萨民兵团', '哥萨正规军']
subOptions = {
    '哥萨民兵团': ['无', '哥萨民兵团'],
    '哥萨正规军': ['无', '哥萨民兵团', '哥萨正规军'],
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