import pandas as pd
import configparser
import os

"""
:param   文件路径,第一行为属性，其余为正则表达式
:return   dict{} key:正则表达式，value:正则所属的属性
"""
def loadExcelDict(file):
    # file = "D:\\work\\结构化\\各类属性总结\\各类属性值.xlsx"
    xl = pd.ExcelFile(file)
    # 所有sheet
    # xl.sheet_names
    dictName = {}
    for name in xl.sheet_names:
        sheet = pd.read_excel(file, name)
        # 替换缺失值
        sheet.fillna("", inplace=True)
        # 所有列
        cols = sheet.columns
        for col in cols:
            if col:
                # 某列下的每个元素
                for word in sheet[col]:
                    if word:
                        dictName[word] = col

    # print(dictName)
    return dictName

def loadExcelDictPd(file):
    xl = pd.ExcelFile(file)
    # 所有sheet
    # xl.sheet_names
    dictName = {}
    for name in xl.sheet_names:
        sheet = pd.read_excel(file, name)
        # 替换缺失值
        sheet.fillna("", inplace=True)
        # 所有列
        cols = sheet.columns
        for col in cols:
            if col:
                # 某列下的每个元素
                for word in sheet[col]:
                    if word:
                        dictName[word] = col
    return dictName

"""
:param file(词典路径) property(词典中每个单词的属性)
return dict(词典)
"""
def loadTxtDict(file, property):
    propertyDict = {}
    f = open(file, encoding="utf-8")
    for words in f:
        propertyDict[words.strip()] = property
    return propertyDict


def loadDict(configFile, sectionKey, sectionValue):
    # 读取配置文件
    root_dir = os.path.dirname(os.path.abspath('.'))
    config_path = os.path.join(root_dir, "config", configFile)
    cf = configparser.ConfigParser()
    cf.read(config_path, encoding="utf-8")
    # 获取名为dictName且key为dictName的value
    dictName = cf.get(sectionKey, sectionValue)
    # 获取所有属性
    properties = dictName.split(",")

    # 加载所有词典
    propertyDict = {}
    for p in properties:
        property_path = os.path.join(root_dir, "config", p)
        print(property_path)
        # excel 字典
        if ".xls" in property_path:
            propertyDict.update(loadExcelDictPd(property_path))
        else:
            # txt字典
            propertyDict.update(loadTxtDict(property_path, p))

    return propertyDict

