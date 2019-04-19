import jieba
from AC.ACAutomationPre import acmation

key = ["殷俊","王志青","范凯"]               #创建模式串
#读取文件，创建模式串
# f = open("D:\\work\\workspace\\eclipse\\ac\\acel\\target\\classes\\dict\\book_name_quan.txt", encoding="utf-8")
# x = 0;
# for line in f:
#     key.append(line)
#     x += 1;
#     if(x%100==0):
#         print(x)

acp = acmation()                                    #类对象
for i in key:
    acp.insert(i)  # 添加模式串

acp.ac_automation()  # 创建fail指针

str = "王志青殷俊王察愁吃范凯愁穿范凯"
#分词操作
str = jieba.cut(str)
str = " ".join(str)
print(str)
resIndex = []
res = acp.runkmp(str)# 查找，输出结果
print("res: ",  res)
#获取起止位置
count = []
for j in key:
    lens = len(j)
    count.append(lens)
for i in res:
    j = i[0] - 1
    k = count[j]
    index01 = i[1] - k + 1
    resIndex.append((i[0],index01,i[1]))
print("resindex: ", resIndex)    #标注有起止位置的数组
strList = list(str)
print("strList : ")
print(strList)
#加尖括号功能
num = 0
domin = "人名" #属性值
for i in resIndex:
    indexPre = i[1] + num
    strList.insert(indexPre,"<")
    num +=1
    indexEnd = i[2] + num+1
    strList.insert(indexEnd, "//人名>")
    num += 1
resStr = "".join(strList) #加完尖括号的字符串
print(resStr)
