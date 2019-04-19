import jieba
import pandas as pd
from utils.DropStropWords import dict_drop_stopwords

#读取分词数据
f = open("D:\\work\\结构化\\art_20190404.txt", encoding="utf-8")
out = open("D:\work\结构化\各类属性总结\\艺术文玩字典词统计.txt", 'w', encoding='utf-8')

#读取停用词
stopwords = pd.read_csv("./../config/stopwords.txt",index_col=False,sep="\t",quoting=3,names=['stopword'], encoding='utf-8')

artDict = {}
i = 1
for line in f:
    for word in jieba.cut(line, cut_all=False):
        # if i > 100:
        #     break
        if word in artDict:
            artDict[word] = artDict[word] + 1
        else:
            print(word+" : "+str(i))
            i += 1
            artDict[word] = 1

newArtDict = dict_drop_stopwords(artDict, stopwords)
# print(type(newArtDict))
for k, v in newArtDict.items():
    out.write(k+"\t"+str(v)+"\n")

f.close()
out.close()
