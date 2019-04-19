import configparser
import os
from AC.ACAutomation import acmation
# 读取配置文件
root_dir = os.path.dirname(os.path.abspath('.'))
config_path = os.path.join(root_dir, "config", "config.ini")
# print("配置文件：" + config_path)
cf = configparser.ConfigParser()
cf.read(config_path, encoding="utf-8")
#获取所有section
secs = cf.sections()
# print(secs)
#获取名为dictName的section的所有key
options = cf.options("dictName")
# print(options)

#获取名为dictName的section的所有key和value
items = cf.items("dictName")
# print(items)

#获取名为dictName且key为dictName的value
dictName = cf.get("dictName", "dictName")
# print(dictName)

#获取所有属性
propertys = dictName.split("，")
# print(propertys)

#######################3
#加载所有词典
propertyDict = {}
for p in propertys:
    property_path = os.path.join(root_dir, "config", p)
    # print(property_path)
    f = open(property_path,encoding="utf-8")
    for words in f:
        propertyDict[words.strip()] = p
#
#AC自动机加载所有词典
ac = acmation()
for k, v in propertyDict.items():
    ac.insert(k, v)
# key = ["龙头","大麟花"]
# for i in key:
#     ac.insert(i,i)  # 添加模式串
# # 构建尾指针
ac.ac_automation()
#
#读取文本，AC匹配
text = open("D:\\work\\结构化\\玩具乐器\\test.txt", encoding="utf-8")
context = "紫檀龙头二胡。 高品质紫檀龙头二胡，选用一级紫檀木料，大麟花"
print(ac.runkmp(context))


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