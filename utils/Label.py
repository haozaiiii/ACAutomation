# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]

# 元素不为空
def secondNotNone(elem):
    return len(elem) > 0

def labelPerson(line, dictName):
    # list 按start排序
    dictName.sort(key=takeSecond)
    # print(dictName.sort(key=takeSecond))
    # 打标签
    num = 0
    newline = list(line)
    for dName in dictName:
        newline.insert(int(dName[1])+num, "<")
        num += 1
        print(dName[1]+num+1)
        newline.insert(dName[1]+len(dName[0])+num, "//"+dName[2]+">")
        num += 1
    return newline

def labelBMES(line, dictName):
    indexDict = {}
    str = ""
    for k in dictName:
        if k:
            # print(k)
            for index in range(len(k[0])):
                indexDict[k[1] + index] = "M_" + k[2]
            indexDict[k[1]] = "B_" + k[2]
            indexDict[k[1] + len(k[0]) - 1] = "E_" + k[2]

    for i in range(len(line)):
        if indexDict.get(i):
            print(repr(indexDict.get(i)))
            print(indexDict.get(i))
            str += line[i] + "\t" + "N" + "\t" + indexDict.get(i) + "\n"
            # str += line[i] + "\t" + indexDict.get(i) + "\n"
        elif line[i]:
            str += line[i] + "\tN\tS\n"
            # str += line[i] + "\tS\n"

    str += "\n"

    return str



