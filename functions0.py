import random

def levelChooser(Text:str, target:str, bottom:int, top:int):
    temp = random.randint(bottom, top)
    Text = Text.replace(target+"（）", target+"（"+str(temp)+"）", 1)
    return Text

def mediumEmpireGeneralChooser(Text:str):
    temp = random.randint(1, 2)
    if temp == 1:
        Text = Text.replace("帝国将军（", "帝国将军（迷诱之盾，")
    else:
        Text = Text.replace("帝国将军（", "帝国将军（符文之牙，")
    temp = random.randint(1, 2)
    if temp == 1:
        Text = Text.replace("帝国将军（", "帝国将军（坚守阵线，致命突袭，")
    else:
        Text = Text.replace("帝国将军（", "帝国将军（索敌者，坚守阵地，")
    return Text

def mediumEmpireCaptainChooser(Text:str):
    temp = random.randint(1, 2)
    if temp == 1:
        Text = Text.replace("帝国队长（", "帝国队长（鲁莽药剂，")
    if temp == 2:
        Text = Text.replace("帝国队长（", "帝国队长（英雄克星剑，")
    temp = random.randint(1, 3)
    if temp == 1:
        Text = Text.replace("帝国队长（", "帝国队长（坚守阵线，")
    if temp == 2:
        Text = Text.replace("帝国队长（", "帝国队长（索敌者，")
    if temp == 3:
        Text = Text.replace("帝国队长（", "帝国队长（致命突袭，")
    return Text

def mediumEmpireHunterChooser(Text:str):
    temp = random.randint(1, 3)
    if temp == 1:
        Text = Text.replace("猎人将军（", "猎人将军（火焰冰雹，")
    if temp == 2:
        Text = Text.replace("猎人将军（", "猎人将军（石油瓶，")
    if temp == 3:
        Text = Text.replace("猎人将军（", "猎人将军（阿克夏之箭，")
    temp = random.randint(1, 2)
    if temp == 1:
        Text = Text.replace("猎人将军（", "猎人将军（闪亮鳞甲，")
    if temp == 2:
        Text = Text.replace("猎人将军（", "猎人将军（命令王冠，")
    return Text