from AC.ACAutomation import loadAC
from AC.EL import findPosition
from utils.ReadData import loadDict
from utils.Label import labelPerson
import jieba

from utils.Label import labelBMES

configFile = "config.ini"
sectionKey = "dictName"
ACsectionValue = "acName"
ELsectionValue = "elName"

#分词操作
jieba.load_userdict("D:\\work\\结构化\\处理\\玩具乐器\\玩具乐器_字典.txt")

#加载AC自动机
acDict = loadDict(configFile, sectionKey, ACsectionValue)
ac = loadAC(acDict)
#加载正则字典
# elDict = loadDict(configFile, sectionKey, ELsectionValue)

#读取文本，AC匹配、EL匹配
text = open("D:\\work\\结构化\\处理\\玩具乐器\\玩具乐器_test.txt", encoding="utf-8")
outBMES = open("D:\\work\\结构化\\处理\\玩具乐器\\玩具乐器_test_标注.txt", 'w', encoding='utf8')
# text = open("D:\\work\\结构化\\train\\pre\\玩具乐器_test.txt", encoding="utf-8")
# outBMES = open("D:\\work\\结构化\\train\\玩具乐器_test.txt", 'w', encoding='utf8')
for line in text:
    # line = line.replace("\t", "")
    line = "|".join(jieba.cut(line))
    result = []
    # AC匹配
    result += ac.runkmp(line)
    # EL匹配
    # result += findPosition(line, elDict)
    #去除空元素
    result = [x for x in result if x]

    #打标签
    newLine = labelPerson(line, result)
    # newLine = labelBMES(line, result)
    outBMES.write("".join(newLine))
    # outBMES.write("".join(newLine) + "\n")

text.close()
outBMES.close()

#读取配置文件，获取所有字典名称
#jieba加载所有字典并分词
#AC自动机匹配
#返回标注数据
#返回BMES数据
