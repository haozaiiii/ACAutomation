from wordseg import WordSegment
# doc = u'十四是十四四十是四十，十四不是四十，四十不是十四'
# ws = WordSegment(doc, max_word_len=2, min_aggregation=1, min_entropy=0.5)
# print(ws.segSentence(doc))
out = open("D:\work\结构化\各类属性总结\\艺术文玩"
           "字典词统计_新词发现.txt", 'w', encoding='utf-8')
with open("D:\\work\\结构化\\art_20190404.txt", encoding='utf-8') as file_object:
    doc = file_object.read()
    # doc = u'十四是十四四十是四十，十四不是四十，四十不是十四'
    # print(type(doc.encode("unicode_escape")))
    ws = WordSegment(doc, max_word_len=6, min_aggregation=10, min_entropy=1.5)
    # out.write("".join(ws.segSentence(doc)))
    # print(words)
    for word in ws.segSentence(doc):
        if(len(word)>1):
            out.write(word+"\n")
