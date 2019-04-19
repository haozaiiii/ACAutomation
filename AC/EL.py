import re
# param:str(字符串)，dict{}(正则表达式字典)
# return: list(匹配到的字符，起始位置，字符属性)
def findPosition(str, els):
    positions = []
    for el, property in els.items():
        res = re.finditer(el, str, re.I)
        if res:
            for r in res:
                if r:
                    positions.append([r.group(), r.start(), property])
    return positions





