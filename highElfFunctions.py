import random

beastSpellDict = ["维杉的狂野形态", "群鸦盛宴", "潘恩的坚硬毛皮", "琥珀之矛", "安拉海尔的诅咒", "卡堂变形术"]
deathSpellDict = ["恐惧骑士化身", "灵魂榨取", "黑暗绝望", "灵魂枯萎", "泽雷斯紫色邪阳", "贝加纳的命运"]
flameSpellDict = ["流火披风", "火球术", "鲁因火焰剑", "烈焰之颅", "烈焰风暴", "穿刺焰矢"]
heavenSpellDict = ["和音汇聚", "风爆术",  "夜风诅咒", "尤瑞诺闪电箭", "连环闪电", "卡莎朵拉彗星"]
highSpellDict = ["神圣颂扬", "荣耀之手", "灵魂淬火", "八风暴雨", "秘法裂解", "万焰燃集"]
liveSpellDict = ["大地之血", "森林复苏", "荆棘护盾", "石化之躯", "再生术", "地灵觉醒"]
lightSpellDict = ["菲的庇护之光", "闪的灼热凝视", "征战之光", "阿明托克之网", "放逐之光", "拜若纳的时光扭曲"]
metalSpellDict = ["毁灭熔流", "锈蚀瘟疫", "吉哈纳的黄金猎犬", "闪耀长袍", "终极炼金术", "铅之炼金术"]
shadowSpellDict = ["虚弱术", "梅尔克斯的迷魂毒瘴", "凋零术", "朦胧钟摆", "奥卡姆的意念剃刀", "幽暗深渊"]
herseSpellDict = ["和音汇聚", "灵魂榨取", "维杉的狂野形态", "大地之血", "梅尔克斯的迷魂毒瘴", "闪的灼热凝视"]

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

#民兵团
def militiaChooser(level:str):
    temp = random.randint(1, 2)
    if temp == 1:
        #精灵贵族选择器
        text="精灵贵族（）"
        if level == '初入战场':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '经验丰富':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（，圣香")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（，星辰护甲")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '久战沙场':
            text = text.replace("精灵贵族（", "精灵贵族（全选")
    elif temp == 2:
        temp = random.randint(1, 9)
        if temp == 1:
            # 精灵法师（野兽系）选择器
            text = "精灵法师（野兽系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，"+tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，星林法杖")
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（" + tempText)
            elif level == '久战沙场':
                options = beastSpellDict[:]
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（全选")
        elif temp == 2:
            # 精灵法师（死亡系）选择器
            text = "精灵法师（死亡系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，"+tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，星林法杖")
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（" + tempText)
            elif level == '久战沙场':
                options = deathSpellDict[:]
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（全选")
        elif temp == 3:
            # 精灵法师（火焰系）选择器
            text = "精灵法师（火焰系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，"+tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，星林法杖")
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（" + tempText)
            elif level == '久战沙场':
                options = flameSpellDict[:]
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（全选")
        elif temp == 4:
            # 精灵法师（天堂系）选择器
            text = "精灵法师（天堂系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，"+tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，星林法杖")
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（" + tempText)
            elif level == '久战沙场':
                options = heavenSpellDict[:]
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（全选")
        elif temp == 5:
            # 精灵法师（高等系）选择器
            text = "精灵法师（高等系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，"+tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，星林法杖")
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（" + tempText)
            elif level == '久战沙场':
                options = highSpellDict[:]
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（全选")
        elif temp == 6:
            # 精灵法师（生命系）选择器
            text = "精灵法师（生命系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，"+tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，星林法杖")
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（" + tempText)
            elif level == '久战沙场':
                options = liveSpellDict[:]
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（全选")
        elif temp == 7:
            # 精灵法师（光明系）选择器
            text = "精灵法师（光明系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，"+tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，星林法杖")
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（" + tempText)
            elif level == '久战沙场':
                options = lightSpellDict[:]
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（全选")
        elif temp == 8:
            # 精灵法师（金属系）选择器
            text = "精灵法师（金属系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，"+tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，星林法杖")
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（" + tempText)
            elif level == '久战沙场':
                options = metalSpellDict[:]
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（全选")
        elif temp == 9:
            # 精灵法师（阴影系）选择器
            text = "精灵法师（阴影系）（）"
            if level == '初入战场':
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，"+tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（"+tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，星林法杖")
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（" + tempText)
            elif level == '久战沙场':
                options = shadowSpellDict[:]
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（全选")

    temp = random.randint(1, 2)
    if temp == 1:
        text += "，长矛兵（），长矛兵（）"
        text = levelChooser(text, "长矛兵", level)
        text = levelChooser(text, "长矛兵", level)
    else:
        text += "，游侠（），游侠（）"
        text = levelChooser(text, "游侠", level)
        text = levelChooser(text, "游侠", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，弓箭手（），弓箭手（）"
        text = levelChooser(text, "弓箭手", level)
        text = levelChooser(text, "弓箭手", level)
    else:
        text += "，弓箭手（重箭）（），弓箭手（重箭）（）"
        text = levelChooser(text, "弓箭手（重箭）", level)
        text = levelChooser(text, "弓箭手（重箭）", level)
    text += "\n"
    return text

#正规军
def regularArmyChooser(level:str):
    temp = random.randint(1, 3)
    if temp == 1:
        #精灵公主选择器
        text = "精灵公主（）"
        if level == '初入战场':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（漫射")
            elif temp == 2:
                text = text.replace("精灵公主（", "精灵公主（索敌者")
            else:
                text = text.replace("精灵公主（", "精灵公主（剑雨齐射")
        elif level == '经验丰富':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（，漫射")
            elif temp == 2:
                text = text.replace("精灵公主（", "精灵公主（，索敌者")
            else:
                text = text.replace("精灵公主（", "精灵公主（，剑雨齐射")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（洛伊克护符")
            else:
                text = text.replace("精灵公主（", "精灵公主（瓦尔号角")
        elif level == '久战沙场':
            text = text.replace("精灵公主（", "精灵公主（全选")
    elif temp == 2:
        # 精灵王子选择器
        text = "精灵王子（）"
        if level == '初入战场':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（索敌者")
            elif temp == 2:
                text = text.replace("精灵王子（", "精灵王子（坚守阵地")
            else:
                text = text.replace("精灵王子（", "精灵王子（不屈不饶")
        elif level == '经验丰富':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（索敌者")
            elif temp == 2:
                text = text.replace("精灵王子（", "精灵王子（坚守阵地")
            else:
                text = text.replace("精灵王子（", "精灵王子（不屈不饶")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（凶兆之盾")
            else:
                text = text.replace("精灵王子（", "精灵王子（贝尔可哈迪斯之剑")
        elif level == '久战沙场':
            text = text.replace("精灵王子（", "精灵王子（全选")
    elif temp == 3:
        temp = random.randint(1, 9)
        if temp == 1:
            # 大法师（野兽系）选择器
            text = "大法师（野兽系）（）"
            if level == '初入战场':
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，野性之心")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，奥术导体")
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，星林法杖")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，野性之心")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，奥术导体")
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（" + tempText)
            elif level == '久战沙场':
                options = beastSpellDict[:]
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（全选")
        elif temp == 2:
            # 大法师（死亡系）选择器
            text = "大法师（死亡系）（）"
            if level == '初入战场':
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，生命虹吸")
                text = text.replace("大法师（野兽系）（", "大法师（死亡系）（，奥术导体")
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，星林法杖")
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，生命虹吸")
                text = text.replace("大法师（野兽系）（", "大法师（死亡系）（，奥术导体")
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（" + tempText)
            elif level == '久战沙场':
                options = deathSpellDict[:]
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（全选")
        elif temp == 3:
            # 大法师（火焰系）选择器
            text = "大法师（火焰系）（）"
            if level == '初入战场':
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，集焰为炎")
                text = text.replace("大法师（野兽系）（", "大法师（火焰系）（，奥术导体")
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，星林法杖")
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，集焰为炎")
                text = text.replace("大法师（野兽系）（", "大法师（火焰系）（，奥术导体")
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（" + tempText)
            elif level == '久战沙场':
                options = flameSpellDict[:]
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（全选")
        elif temp == 4:
            # 大法师（天堂系）选择器
            text = "大法师（天堂系）（）"
            if level == '初入战场':
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，天空乱流")
                text = text.replace("大法师（野兽系）（", "大法师（天堂系）（，奥术导体")
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，星林法杖")
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，天空乱流")
                text = text.replace("大法师（野兽系）（", "大法师（天堂系）（，奥术导体")
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（" + tempText)
            elif level == '久战沙场':
                options = heavenSpellDict[:]
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（全选")
        elif temp == 5:
            # 大法师（高等系）选择器
            text = "大法师（高等系）（）"
            if level == '初入战场':
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，萨芙睿之盾")
                text = text.replace("大法师（野兽系）（", "大法师（高等系）（，奥术导体")
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（高等系）（", "大法师（高等系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（高等系）（", "大法师（高等系）（，星林法杖")
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，萨芙睿之盾")
                text = text.replace("大法师（野兽系）（", "大法师（高等系）（，奥术导体")
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（" + tempText)
            elif level == '久战沙场':
                options = highSpellDict[:]
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                text = text.replace("大法师（高等系）（", "大法师（高等系）（全选")
        elif temp == 6:
            # 大法师（生命系）选择器
            text = "大法师（生命系）（）"
            if level == '初入战场':
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，生命绽放")
                text = text.replace("大法师（野兽系）（", "大法师（生命系）（，奥术导体")
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（生命系）（", "大法师（生命系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（生命系）（", "大法师（生命系）（，星林法杖")
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，生命绽放")
                text = text.replace("大法师（野兽系）（", "大法师（生命系）（，奥术导体")
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（" + tempText)
            elif level == '久战沙场':
                options = liveSpellDict[:]
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                text = text.replace("大法师（生命系）（", "大法师（生命系）（全选")
        elif temp == 7:
            # 大法师（光明系）选择器
            text = "大法师（光明系）（）"
            if level == '初入战场':
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，驱除邪魔")
                text = text.replace("大法师（野兽系）（", "大法师（光明系）（，奥术导体")
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（光明系）（", "大法师（光明系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（光明系）（", "大法师（光明系）（，星林法杖")
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，驱除邪魔")
                text = text.replace("大法师（野兽系）（", "大法师（光明系）（，奥术导体")
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（" + tempText)
            elif level == '久战沙场':
                options = lightSpellDict[:]
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                text = text.replace("大法师（光明系）（", "大法师（光明系）（全选")
        elif temp == 8:
            # 大法师（金属系）选择器
            text = "大法师（金属系）（）"
            if level == '初入战场':
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，金属转化")
                text = text.replace("大法师（野兽系）（", "大法师（金属系）（，奥术导体")
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（金属系）（", "大法师（金属系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（金属系）（", "大法师（金属系）（，星林法杖")
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，金属转化")
                text = text.replace("大法师（野兽系）（", "大法师（金属系）（，奥术导体")
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（" + tempText)
            elif level == '久战沙场':
                options = metalSpellDict[:]
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                text = text.replace("大法师（金属系）（", "大法师（金属系）（全选")
        elif temp == 9:
            # 大法师（阴影系）选择器
            text = "大法师（阴影系）（）"
            if level == '初入战场':
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，虚无幻象")
                text = text.replace("大法师（野兽系）（", "大法师（阴影系）（，奥术导体")
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，星林法杖")
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，虚无幻象")
                text = text.replace("大法师（野兽系）（", "大法师（阴影系）（，奥术导体")
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（" + tempText)
            elif level == '久战沙场':
                options = shadowSpellDict[:]
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（全选")

    text += "，银光守卫（），银光守卫（）"
    text = levelChooser(text, "银光守卫", level)
    text = levelChooser(text, "银光守卫", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，弓箭手（），弓箭手（）"
        text = levelChooser(text, "弓箭手", level)
        text = levelChooser(text, "弓箭手", level)
    else:
        text += "，弓箭手（重箭）（），弓箭手（重箭）（）"
        text = levelChooser(text, "弓箭手（重箭）", level)
        text = levelChooser(text, "弓箭手（重箭）", level)
    text += "\n"
    return text

#洛瑟恩海卫
def roserenGuardChooser(level:str):
    # 精灵公主选择器
    text = "精灵公主（）"
    if level == '初入战场':
        temp = random.randint(1, 3)
        if temp == 1:
            text = text.replace("精灵公主（", "精灵公主（漫射")
        elif temp == 2:
            text = text.replace("精灵公主（", "精灵公主（索敌者")
        else:
            text = text.replace("精灵公主（", "精灵公主（剑雨齐射")
    elif level == '经验丰富':
        temp = random.randint(1, 3)
        if temp == 1:
            text = text.replace("精灵公主（", "精灵公主（，漫射")
        elif temp == 2:
            text = text.replace("精灵公主（", "精灵公主（，索敌者")
        else:
            text = text.replace("精灵公主（", "精灵公主（，剑雨齐射")
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("精灵公主（", "精灵公主（洛伊克护符")
        else:
            text = text.replace("精灵公主（", "精灵公主（瓦尔号角")
    elif level == '久战沙场':
        text = text.replace("精灵公主（", "精灵公主（全选")

    text += "，洛瑟恩海卫（），洛瑟恩海卫（）"
    text = levelChooser(text, "洛瑟恩海卫", level)
    text = levelChooser(text, "洛瑟恩海卫", level)
    text += "，洛瑟恩海卫（持盾）（），洛瑟恩海卫（持盾）（）"
    text = levelChooser(text, "洛瑟恩海卫（持盾）", level)
    text = levelChooser(text, "洛瑟恩海卫（持盾）", level)
    text += "\n"
    return text

#查瑞斯禁卫
def charesGuardChooser(level:str):
    #白狮选择器
    text = "白狮阿拉斯塔（）"
    if level == '初入战场':
        temp = random.randint(1, 3)
        if temp == 1:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（索敌者")
        elif temp == 2:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（英武必杀")
        else:
            text = text.replace("白狮阿拉斯塔（", "精灵公主（坚守阵地")
    elif level == '经验丰富':
        text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（，白狮战车")
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（，红宝石凤凰守卫")
        else:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（，鲁莽药剂")
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（索敌者")
        elif temp == 2:
            text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（英武必杀")
    else:
        text = text.replace("白狮阿拉斯塔（", "白狮阿拉斯塔（全选，白狮战车")

    text += ", 查瑞斯禁卫（），查瑞斯禁卫（）"
    text = levelChooser(text, "查瑞斯禁卫", level)
    text = levelChooser(text, "查瑞斯禁卫", level)
    if level == '初入战场':
        text += ", 查瑞斯战狮（），查瑞斯战狮（）"
        text = levelChooser(text, "查瑞斯战狮", level)
        text = levelChooser(text, "查瑞斯战狮", level)
    elif level == '经验丰富':
        text += ", 查瑞斯战狮（），查瑞斯战车（）"
        text = levelChooser(text, "查瑞斯战狮", level)
        text = levelChooser(text, "查瑞斯战车", level)
    elif level == '久战沙场':
        text += ", 查瑞斯战车（），查瑞斯战车（）"
        text = levelChooser(text, "查瑞斯战车", level)
        text = levelChooser(text, "查瑞斯战车", level)
    text += "\n"
    return text

#艾里昂掠夺者
def alyonRaiderChooser(level:str):
    temp = random.randint(1, 2)
    if temp == 1:
        # 精灵贵族（马）选择器
        text = "精灵贵族（，银战马）"
        if level == '初入战场':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '经验丰富':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（，圣香")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（，星辰护甲")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '久战沙场':
            text = text.replace("精灵贵族（", "精灵贵族（全选")
    elif temp == 2:
        temp = random.randint(1, 9)
        if temp == 1:
            # 精灵法师（野兽系）选择器
            text = "精灵法师（野兽系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，星林法杖")
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（" + tempText)
            elif level == '久战沙场':
                options = beastSpellDict[:]
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（全选")
        elif temp == 2:
            # 精灵法师（死亡系）选择器
            text = "精灵法师（死亡系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，星林法杖")
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（" + tempText)
            elif level == '久战沙场':
                options = deathSpellDict[:]
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（全选")
        elif temp == 3:
            # 精灵法师（火焰系）选择器
            text = "精灵法师（火焰系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，星林法杖")
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（" + tempText)
            elif level == '久战沙场':
                options = flameSpellDict[:]
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（全选")
        elif temp == 4:
            # 精灵法师（天堂系）选择器
            text = "精灵法师（天堂系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，星林法杖")
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（" + tempText)
            elif level == '久战沙场':
                options = heavenSpellDict[:]
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（全选")
        elif temp == 5:
            # 精灵法师（高等系）选择器
            text = "精灵法师（高等系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，星林法杖")
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（" + tempText)
            elif level == '久战沙场':
                options = highSpellDict[:]
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（全选")
        elif temp == 6:
            # 精灵法师（生命系）选择器
            text = "精灵法师（生命系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，星林法杖")
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（" + tempText)
            elif level == '久战沙场':
                options = liveSpellDict[:]
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（全选")
        elif temp == 7:
            # 精灵法师（光明系）选择器
            text = "精灵法师（光明系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，星林法杖")
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（" + tempText)
            elif level == '久战沙场':
                options = lightSpellDict[:]
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（全选")
        elif temp == 8:
            # 精灵法师（金属系）选择器
            text = "精灵法师（金属系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，星林法杖")
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（" + tempText)
            elif level == '久战沙场':
                options = metalSpellDict[:]
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（全选")
        elif temp == 9:
            # 精灵法师（阴影系）选择器
            text = "精灵法师（阴影系）（，银战马）"
            if level == '初入战场':
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，星林法杖")
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（" + tempText)
            elif level == '久战沙场':
                options = shadowSpellDict[:]
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（全选")

    text += ", 艾里昂掠夺者（），艾里昂掠夺者（）"
    text = levelChooser(text, "艾里昂掠夺者", level)
    text = levelChooser(text, "艾里昂掠夺者", level)
    text += ", 艾里昂掠夺者弓箭手（），艾里昂掠夺者弓箭手（）"
    text = levelChooser(text, "艾里昂掠夺者弓箭手", level)
    text = levelChooser(text, "艾里昂掠夺者弓箭手", level)
    text += "\n"
    return text

def herseChooser(level:str):
    #荷斯魔剑士选择器
    text = "荷斯魔剑士（）"
    if level == '初入战场':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，闪避")
        elif temp == 2:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，索敌者")
        tempText = random.sample(herseSpellDict, k=2)
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[0])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（" + tempText[1])
    elif level == '经验丰富':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，魔剑士披风")
        elif temp == 2:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，赐福卷册")
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，闪避")
        elif temp == 2:
            text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，索敌者")
        tempText = random.sample(herseSpellDict, k=3)
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[0])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[1])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（" + tempText[2])
    elif level == '久战沙场':
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，全选")
        tempText = random.sample(herseSpellDict, k=4)
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[0])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[1])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（，" + tempText[2])
        text = text.replace("荷斯魔剑士（", "荷斯魔剑士（" + tempText[3])

    text += "，荷斯剑圣（），荷斯剑圣（）"
    text = levelChooser(text, "荷斯剑圣", level)
    text = levelChooser(text, "荷斯剑圣", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，弓箭手（），弓箭手（）"
        text = levelChooser(text, "弓箭手", level)
        text = levelChooser(text, "弓箭手", level)
    else:
        text += "，弓箭手（重箭）（），弓箭手（重箭）（）"
        text = levelChooser(text, "弓箭手（重箭）", level)
        text = levelChooser(text, "弓箭手（重箭）", level)
    text += "\n"
    return text

#鹰爪弩炮团
def eagleClawCrossbowChooeser(level:str):
    # 精灵贵族选择器
    text = "精灵贵族（）"
    if level == '初入战场':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("精灵贵族（", "精灵贵族（索敌者")
        else:
            text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
    elif level == '经验丰富':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("精灵贵族（", "精灵贵族（，圣香")
        else:
            text = text.replace("精灵贵族（", "精灵贵族（，星辰护甲")
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("精灵贵族（", "精灵贵族（索敌者")
        else:
            text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
    elif level == '久战沙场':
        text = text.replace("精灵贵族（", "精灵贵族（全选")

    text += "，长矛兵（），长矛兵（）"
    text = levelChooser(text, "长矛兵", level)
    text = levelChooser(text, "长矛兵", level)
    text += "，鹰爪弩炮（），鹰爪弩炮（）"
    text = levelChooser(text, "鹰爪弩炮", level)
    text = levelChooser(text, "鹰爪弩炮", level)
    text += "\n"
    return text

#影子军团
def shadowArmyChooser(level:str):
    #影冠之手选择器
    text = "影冠之手（）"
    if level == '经验丰富':
        temp = random.randint(1, 2)
        if temp == 1:
            text = text.replace("影冠之手（", "影冠之手（漫射")
        else:
            text = text.replace("影冠之手（", "影冠之手（灵活")
    elif level == '久战沙场':
        text = text.replace("影冠之手（", "影冠之手（全选")

    text += "，影子战士（），影子战士（）"
    text = levelChooser(text, "影子战士", level)
    text = levelChooser(text, "影子战士", level)
    temp = random.randint(1, 2)
    if temp == 1:
        text += "，影行者战团（），影行者战团（）"
        text = levelChooser(text, "影行者战团", level)
        text = levelChooser(text, "影行者战团", level)
    elif temp == 2:
        text += "，影子漫游者（），影子漫游者（）"
        text = levelChooser(text, "影子漫游者", level)
        text = levelChooser(text, "影子漫游者", level)
    text += "\n"
    return text

#银盔骑士团
def silverHelmKnightChooser(level:str):
    temp = random.randint(1, 3)
    if temp == 1:
        # 精灵公主（马）选择器
        text = "精灵公主（，银战马）"
        if level == '初入战场':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（漫射")
            elif temp == 2:
                text = text.replace("精灵公主（", "精灵公主（索敌者")
            else:
                text = text.replace("精灵公主（", "精灵公主（剑雨齐射")
        elif level == '经验丰富':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（，漫射")
            elif temp == 2:
                text = text.replace("精灵公主（", "精灵公主（，索敌者")
            else:
                text = text.replace("精灵公主（", "精灵公主（，剑雨齐射")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵公主（", "精灵公主（洛伊克护符")
            else:
                text = text.replace("精灵公主（", "精灵公主（瓦尔号角")
        elif level == '久战沙场':
            text = text.replace("精灵公主（", "精灵公主（全选")
    elif temp == 2:
        # 精灵王子（马）选择器
        text = "精灵王子（，银战马）"
        if level == '初入战场':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（索敌者")
            elif temp == 2:
                text = text.replace("精灵王子（", "精灵王子（坚守阵地")
            else:
                text = text.replace("精灵王子（", "精灵王子（不屈不饶")
        elif level == '经验丰富':
            temp = random.randint(1, 3)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（索敌者")
            elif temp == 2:
                text = text.replace("精灵王子（", "精灵王子（坚守阵地")
            else:
                text = text.replace("精灵王子（", "精灵王子（不屈不饶")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵王子（", "精灵王子（凶兆之盾")
            else:
                text = text.replace("精灵王子（", "精灵王子（贝尔可哈迪斯之剑")
        elif level == '久战沙场':
            text = text.replace("精灵王子（", "精灵王子（全选")
    elif temp == 3:
        temp = random.randint(1, 9)
        if temp == 1:
            # 大法师（野兽系）（马）选择器
            text = "大法师（野兽系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，野性之心")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，奥术导体")
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，星林法杖")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，野性之心")
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，奥术导体")
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（" + tempText)
            elif level == '久战沙场':
                options = beastSpellDict[:]
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（，" + tempText)
                text = text.replace("大法师（野兽系）（", "大法师（野兽系）（全选")
        elif temp == 2:
            # 大法师（死亡系）（马）选择器
            text = "大法师（死亡系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，生命虹吸")
                text = text.replace("大法师（野兽系）（", "大法师（死亡系）（，奥术导体")
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，星林法杖")
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，生命虹吸")
                text = text.replace("大法师（野兽系）（", "大法师（死亡系）（，奥术导体")
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（" + tempText)
            elif level == '久战沙场':
                options = deathSpellDict[:]
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（，" + tempText)
                text = text.replace("大法师（死亡系）（", "大法师（死亡系）（全选")
        elif temp == 3:
            # 大法师（火焰系）选择器
            text = "大法师（火焰系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，集焰为炎")
                text = text.replace("大法师（野兽系）（", "大法师（火焰系）（，奥术导体")
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，星林法杖")
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，集焰为炎")
                text = text.replace("大法师（野兽系）（", "大法师（火焰系）（，奥术导体")
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（" + tempText)
            elif level == '久战沙场':
                options = flameSpellDict[:]
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（，" + tempText)
                text = text.replace("大法师（火焰系）（", "大法师（火焰系）（全选")
        elif temp == 4:
            # 大法师（天堂系）选择器
            text = "大法师（天堂系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，天空乱流")
                text = text.replace("大法师（野兽系）（", "大法师（天堂系）（，奥术导体")
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，星林法杖")
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，天空乱流")
                text = text.replace("大法师（野兽系）（", "大法师（天堂系）（，奥术导体")
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（" + tempText)
            elif level == '久战沙场':
                options = heavenSpellDict[:]
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（，" + tempText)
                text = text.replace("大法师（天堂系）（", "大法师（天堂系）（全选")
        elif temp == 5:
            # 大法师（高等系）选择器
            text = "大法师（高等系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，萨芙睿之盾")
                text = text.replace("大法师（野兽系）（", "大法师（高等系）（，奥术导体")
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（高等系）（", "大法师（高等系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（高等系）（", "大法师（高等系）（，星林法杖")
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，萨芙睿之盾")
                text = text.replace("大法师（野兽系）（", "大法师（高等系）（，奥术导体")
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（" + tempText)
            elif level == '久战沙场':
                options = highSpellDict[:]
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（高等系）（", "大法师（高等系）（，" + tempText)
                text = text.replace("大法师（高等系）（", "大法师（高等系）（全选")
        elif temp == 6:
            # 大法师（生命系）选择器
            text = "大法师（生命系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，生命绽放")
                text = text.replace("大法师（野兽系）（", "大法师（生命系）（，奥术导体")
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（生命系）（", "大法师（生命系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（生命系）（", "大法师（生命系）（，星林法杖")
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，生命绽放")
                text = text.replace("大法师（野兽系）（", "大法师（生命系）（，奥术导体")
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（" + tempText)
            elif level == '久战沙场':
                options = liveSpellDict[:]
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（生命系）（", "大法师（生命系）（，" + tempText)
                text = text.replace("大法师（生命系）（", "大法师（生命系）（全选")
        elif temp == 7:
            # 大法师（光明系）选择器
            text = "大法师（光明系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，驱除邪魔")
                text = text.replace("大法师（野兽系）（", "大法师（光明系）（，奥术导体")
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（光明系）（", "大法师（光明系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（光明系）（", "大法师（光明系）（，星林法杖")
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，驱除邪魔")
                text = text.replace("大法师（野兽系）（", "大法师（光明系）（，奥术导体")
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（" + tempText)
            elif level == '久战沙场':
                options = lightSpellDict[:]
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（光明系）（", "大法师（光明系）（，" + tempText)
                text = text.replace("大法师（光明系）（", "大法师（光明系）（全选")
        elif temp == 8:
            # 大法师（金属系）选择器
            text = "大法师（金属系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，金属转化")
                text = text.replace("大法师（野兽系）（", "大法师（金属系）（，奥术导体")
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（金属系）（", "大法师（金属系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（金属系）（", "大法师（金属系）（，星林法杖")
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，金属转化")
                text = text.replace("大法师（野兽系）（", "大法师（金属系）（，奥术导体")
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（" + tempText)
            elif level == '久战沙场':
                options = metalSpellDict[:]
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（金属系）（", "大法师（金属系）（，" + tempText)
                text = text.replace("大法师（金属系）（", "大法师（金属系）（全选")
        elif temp == 9:
            # 大法师（阴影系）选择器
            text = "大法师（阴影系）（，银战马）"
            if level == '初入战场':
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，虚无幻象")
                text = text.replace("大法师（野兽系）（", "大法师（阴影系）（，奥术导体")
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，星林法杖")
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，虚无幻象")
                text = text.replace("大法师（野兽系）（", "大法师（阴影系）（，奥术导体")
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（" + tempText)
            elif level == '久战沙场':
                options = shadowSpellDict[:]
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（，" + tempText)
                text = text.replace("大法师（阴影系）（", "大法师（阴影系）（全选")

    text += "，银盔骑士（持剑）（），银盔骑士（持剑）（）"
    text = levelChooser(text, "银盔骑士（持剑）", level)
    text = levelChooser(text, "银盔骑士（持剑）", level)
    text += "，银盔骑士（骑枪）（），银盔骑士（骑枪）（）"
    text = levelChooser(text, "银盔骑士（骑枪）", level)
    text = levelChooser(text, "银盔骑士（骑枪）", level)
    text += "\n"
    return text

#银战车团
def silverTankChooser(level:str):
    temp = random.randint(1,3)
    if temp == 1:
        text = "精灵贵族（银战车）"
        if level == '初入战场':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '经验丰富':
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（，圣香")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（，星辰护甲")
            temp = random.randint(1, 2)
            if temp == 1:
                text = text.replace("精灵贵族（", "精灵贵族（索敌者")
            else:
                text = text.replace("精灵贵族（", "精灵贵族（致命突袭")
        elif level == '久战沙场':
            text = text.replace("精灵贵族（", "精灵贵族（全选")
    elif temp == 2:
        temp = random.randint(1, 9)
        if temp == 1:
            # 精灵法师（野兽系）选择器
            text = "精灵法师（野兽系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，星林法杖")
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，野性之心")
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（" + tempText)
            elif level == '久战沙场':
                options = beastSpellDict[:]
                tempText = random.choice(beastSpellDict[4:6])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[2:4])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(beastSpellDict[0:2])
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（，" + tempText)
                text = text.replace("精灵法师（野兽系）（", "精灵法师（野兽系）（全选")
        elif temp == 2:
            # 精灵法师（死亡系）选择器
            text = "精灵法师（死亡系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，星林法杖")
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，生命虹吸")
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（" + tempText)
            elif level == '久战沙场':
                options = deathSpellDict[:]
                tempText = random.choice(deathSpellDict[4:6])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[2:4])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(deathSpellDict[0:2])
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（，" + tempText)
                text = text.replace("精灵法师（死亡系）（", "精灵法师（死亡系）（全选")
        elif temp == 3:
            # 精灵法师（火焰系）选择器
            text = "精灵法师（火焰系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，星林法杖")
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，集焰为炎")
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（" + tempText)
            elif level == '久战沙场':
                options = flameSpellDict[:]
                tempText = random.choice(flameSpellDict[4:6])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[2:4])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(flameSpellDict[0:2])
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（，" + tempText)
                text = text.replace("精灵法师（火焰系）（", "精灵法师（火焰系）（全选")
        elif temp == 4:
            # 精灵法师（天堂系）选择器
            text = "精灵法师（天堂系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，星林法杖")
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，天空乱流")
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（" + tempText)
            elif level == '久战沙场':
                options = heavenSpellDict[:]
                tempText = random.choice(heavenSpellDict[4:6])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(heavenSpellDict[0:2])
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（，" + tempText)
                text = text.replace("精灵法师（天堂系）（", "精灵法师（天堂系）（全选")
        elif temp == 5:
            # 精灵法师（高等系）选择器
            text = "精灵法师（高等系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，星林法杖")
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，萨芙睿之盾")
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(heavenSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（" + tempText)
            elif level == '久战沙场':
                options = highSpellDict[:]
                tempText = random.choice(highSpellDict[4:6])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[2:4])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(highSpellDict[0:2])
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（，" + tempText)
                text = text.replace("精灵法师（高等系）（", "精灵法师（高等系）（全选")
        elif temp == 6:
            # 精灵法师（生命系）选择器
            text = "精灵法师（生命系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，星林法杖")
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，生命绽放")
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（" + tempText)
            elif level == '久战沙场':
                options = liveSpellDict[:]
                tempText = random.choice(liveSpellDict[4:6])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[2:4])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(liveSpellDict[0:2])
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（，" + tempText)
                text = text.replace("精灵法师（生命系）（", "精灵法师（生命系）（全选")
        elif temp == 7:
            # 精灵法师（光明系）选择器
            text = "精灵法师（光明系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，星林法杖")
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，驱除邪魔")
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（" + tempText)
            elif level == '久战沙场':
                options = lightSpellDict[:]
                tempText = random.choice(lightSpellDict[4:6])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[2:4])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(lightSpellDict[0:2])
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（，" + tempText)
                text = text.replace("精灵法师（光明系）（", "精灵法师（光明系）（全选")
        elif temp == 8:
            # 精灵法师（金属系）选择器
            text = "精灵法师（金属系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，星林法杖")
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，金属转化")
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（" + tempText)
            elif level == '久战沙场':
                options = metalSpellDict[:]
                tempText = random.choice(metalSpellDict[4:6])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[2:4])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(metalSpellDict[0:2])
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（，" + tempText)
                text = text.replace("精灵法师（金属系）（", "精灵法师（金属系）（全选")
        elif temp == 9:
            # 精灵法师（阴影系）选择器
            text = "精灵法师（阴影系）（银战车）"
            if level == '初入战场':
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（" + tempText)
            elif level == '经验丰富':
                temp = random.randint(1, 2)
                if temp == 1:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，荷斯之书")
                elif temp == 2:
                    text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，星林法杖")
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，虚无幻象")
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（" + tempText)
            elif level == '久战沙场':
                options = shadowSpellDict[:]
                tempText = random.choice(shadowSpellDict[4:6])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[2:4])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(shadowSpellDict[0:2])
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                options.remove(tempText)
                tempText = random.choice(options)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（，" + tempText)
                text = text.replace("精灵法师（阴影系）（", "精灵法师（阴影系）（全选")