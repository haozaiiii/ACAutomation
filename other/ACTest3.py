import jieba
from AC.ACAutomationPre import acmation

def sparate(str, out):
    # str = jieba.cut(str)
    # str = " ".join(str)
    # print(str)
    resIndex = []
    res = acp.runkmp(str)  # 查找，输出结果
    # print("res: ", res)
    # 获取起止位置
    count = []
    for j in key:
        lens = len(j)
        count.append(lens)
    for i in res:
        j = i[0] - 1
        k = count[j]
        index01 = i[1] - k + 1
        resIndex.append((i[0], index01, i[1]))
    # print("resindex: ", resIndex)  # 标注有起止位置的数组
    strList = list(str)
    # print("strList : ")
    print(strList)
    # 加尖括号功能
    num = 0
    domin = "人名"  # 属性值
    for i in resIndex:
        indexPre = i[1] + num
        strList.insert(indexPre, "<")
        num += 1
        indexEnd = i[2] + num + 1
        strList.insert(indexEnd, "//键数>")
        num += 1
    resStr = "".join(strList)  # 加完尖括号的字符串
    out.write(resStr)
    # print(resStr)
# strat
f = open("D:\\work\\workspace\\pycharm\\InfoExtraction\\config\\键数", encoding="utf-8")
key = []
for line in f:
    key.append(line.strip())
#创建模式串
acp = acmation()                                    #类对象
for i in key:
    acp.insert(i)  # 添加模式串

acp.ac_automation()  # 创建fail指针

#分词操作
# jieba.load_userdict("D:\\work\\workspace\\pycharm\\InfoExtraction\\config\\材质")
texts = open("D:\\work\\结构化\\处理\\乐器_品牌_材质_种类_规格.txt", encoding="utf-8")
out = open('D:\\work\\结构化\\处理\\乐器_品牌_材质_种类_规格_键数.txt', 'w', encoding='utf8')
for text in texts:
    # str = text.split("\t")[3]+text.split("\t")[4]
    str = text
    print(str)
    sparate(str, out)

texts.close()
out.close()
