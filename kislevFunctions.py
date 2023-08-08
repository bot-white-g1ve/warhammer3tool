import random

boyeSkillDict = ["英武复原", "索敌者", "致命突袭", "坚守阵地"]

def levelChooser(Text:str, target:str, level:str):
    if level == '初入战场':
        n = 1
    elif level == '经验丰富':
        n = 4
    elif level == '久战沙场':
        n = 7
    temp = random.randint(n, n+2)
    Text = Text.replace(target+"（）", target+"（"+str(temp)+"）", 1)
    return Text

#哥萨民兵团
def gosaMilitiaChooser(level:str):
    #波耶选择器
    text = "波耶（）"
    if level == '初入战场':
        tempText = random.choice(boyeSkillDict)
        text = text.replace("波耶（", "波耶（"+tempText)
    elif level == '经验丰富':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("波耶（", "波耶（，祖国母亲之血")
        elif temp == 2:
            text = text.replace("波耶（", "波耶（，托尔战斧")
        tempText = random.sample(boyeSkillDict, k=2)
        text = text.replace("波耶（", "波耶（，" + tempText[0])
        text = text.replace("波耶（", "波耶（" + tempText[1])
    elif level == '久战沙场':
        text = text.replace("波耶（", "波耶（，物品全选")
        tempText = random.sample(boyeSkillDict, k=3)
        text = text.replace("波耶（", "波耶（，" + tempText[0])
        text = text.replace("波耶（", "波耶（，" + tempText[1])
        text = text.replace("波耶（", "波耶（" + tempText[2])

    text += "，哥萨（刀盾）（），哥萨（刀盾）（）"
    text = levelChooser(text, "哥萨（刀盾）", level)
    text = levelChooser(text, "哥萨（刀盾）", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，哥萨（），哥萨（）"
        text = levelChooser(text, "哥萨", level)
        text = levelChooser(text, "哥萨", level)
    elif temp == 2:
        text += "，哥萨（持矛）（），哥萨（持矛）（）"
        text = levelChooser(text, "哥萨（持矛）", level)
        text = levelChooser(text, "哥萨（持矛）", level)
    text += "\n"
    return text

def gosaRegularArmyChooser(level:str):
    # 波耶选择器
    text = "波耶（）"
    if level == '初入战场':
        tempText = random.choice(boyeSkillDict)
        text = text.replace("波耶（", "波耶（" + tempText)
    elif level == '经验丰富':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("波耶（", "波耶（，祖国母亲之血")
        elif temp == 2:
            text = text.replace("波耶（", "波耶（，托尔战斧")
        tempText = random.sample(boyeSkillDict, k=2)
        text = text.replace("波耶（", "波耶（，" + tempText[0])
        text = text.replace("波耶（", "波耶（" + tempText[1])
    elif level == '久战沙场':
        text = text.replace("波耶（", "波耶（，物品全选")
        tempText = random.sample(boyeSkillDict, k=3)
        text = text.replace("波耶（", "波耶（，" + tempText[0])
        text = text.replace("波耶（", "波耶（，" + tempText[1])
        text = text.replace("波耶（", "波耶（" + tempText[2])

    temp = random.randint(1, 2)
    if temp == 1:
        text += "，披甲哥萨（），披甲哥萨（）"
        text = levelChooser(text, "披甲哥萨", level)
        text = levelChooser(text, "披甲哥萨", level)
    elif temp == 2:
        text += "，披甲哥萨（重型武器）（），披甲哥萨（重型武器）（）"
        text = levelChooser(text, "披甲哥萨（重型武器）", level)
        text = levelChooser(text, "披甲哥萨（重型武器）", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，射击军（），射击军（）"
        text = levelChooser(text, "射击军", level)
        text = levelChooser(text, "射击军", level)
    elif temp == 2:
        text += "，射击军（月牙斧）（），射击军（月牙斧）（）"
        text = levelChooser(text, "射击军（月牙斧）", level)
        text = levelChooser(text, "射击军（月牙斧）", level)
    text += "\n"
    return text