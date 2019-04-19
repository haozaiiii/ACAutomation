import configparser
import os
from AC.ACAutomation import acmation

def loadAC(configFile, sectionKey, sectionValue):
    # 读取配置文件
    root_dir = os.path.dirname(os.path.abspath('.'))
    config_path = os.path.join(root_dir, "config", configFile)
    print("配置文件：" + config_path)
    cf = configparser.ConfigParser()
    cf.read(config_path, encoding="utf-8")
    #获取名为dictName且key为dictName的value
    dictName = cf.get(sectionKey, sectionValue)
    #获取所有属性
    propertys = dictName.split("，")

    #加载所有词典
    propertyDict = {}
    for p in propertys:
        property_path = os.path.join(root_dir, "config", p)
        # print(property_path)
        f = open(property_path,encoding="utf-8")
        for words in f:
            propertyDict[words.strip()] = p

    #AC自动机加载所有词典
    ac = acmation()
    for k, v in propertyDict.items():
        # 添加模式串
        ac.insert(k, v)

    # 构建尾指针
    ac.ac_automation()

    return ac

#获取AC自动机
configFile = "config.ini"
sectionKey = "dictName"
sectionValue = "dictName"
ac = loadAC(configFile, sectionKey, sectionValue)

#读取文本，AC匹配
text = open("D:\\work\\结构化\\玩具乐器\\test.txt", encoding="utf-8")
outBMES = open("D:\\work\\结构化\\处理\\BMES_musical.txt", 'w', encoding='utf8')
for line in text:
    # print(kmpList)
    indexDict = {}
    for k in ac.runkmp(line):
        if k:
            print(k)
            for index in range(len(k[0])):
                indexDict[k[1]+index] = "M_" + k[2]
            indexDict[k[1]] = "B_" + k[2]
            indexDict[k[1]+len(k[0])-1] = "E_" + k[2]
    print(indexDict)
    for i in range(len(line)):
        if indexDict.get(i):
            outBMES.write(line[i] + "\t" + repr(indexDict.get(i)) + "\n")
        elif line[i]:
            outBMES.write(line[i] + "\tS\n")

    outBMES.write("\n")



text.close()
outBMES.close()


            # print(len(k[0]))
    #     print()
    # kmpSet = {}
    # listKmp = ac.runkmp(line)
    # print(ac.runkmp(line))


# context = "紫檀龙头二胡。 高品质紫檀龙头二胡，选用一级紫檀木料，大麟花"


# for line in text:
    # print(line)
    # result = ac.runkmp(line)
    # print(result)
    # print(line)
    # print(result)



#读取配置文件，获取所有字典名称
#jieba加载所有字典并分词
#AC自动机匹配
#返回标注数据
#返回BMES数据
