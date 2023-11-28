import jieba

words = """ ### jieba ———— 分词
#### 模式
1. 精确
2. 全模式
3. 搜索引擎模式 """

cuted_words = jieba.lcut(words)
# print(cuted_words.count("模式"))
# 3

set_words = set(cuted_words)
for i in set_words:
    n = cuted_words.count(i)
    print(i, "......", n)
''' 
— ...... 4
分词 ...... 1
. ...... 3
全 ...... 1
jieba ...... 1
2 ...... 1
模式 ...... 3
搜索引擎 ...... 1
  ...... 9
#### ...... 1

 ...... 4
1 ...... 1
精确 ...... 1
### ...... 1
3 ...... 1
'''
