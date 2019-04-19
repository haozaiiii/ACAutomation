#去除停用词
#传入的数据需为contents:list of list |  stopwords:list
#传出的数据为contents_clean:list of list  |   all_words:list
def drop_stopwords(contents, stopwords):
    contents_clean = []
    all_words = []
    for line in contents:
        line_clean = []
        for word in line:
            if word in stopwords:
                continue
            line_clean.append(word)
            all_words.append(str(word))
        contents_clean.append(line_clean)
    return contents_clean, all_words

# 删除dict中的停用词
def dict_drop_stopwords(wordDict, stopwords):
    for k in wordDict:
        if k in stopwords:
            wordDict.remove(k)
    return wordDict