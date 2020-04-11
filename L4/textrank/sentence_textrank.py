# -*- coding: utf-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg

sentence = '王者荣耀典韦连招是使用一技能+大招+晕眩+二技能+普攻，这套连招主要用于先手强开团，当发现对面走位失误或撤退不及时，我们就可以利用一技能的加速，配合大招减速留住对手，协同队友完成击杀。当对方站位较集中时，我们同样可以利用“一技能+大招+晕眩”进行团控和吸收伤害。在吸收伤害的同时我们还可以利二技能打出不错的输出。这套连招重要的是把握时机，要有一夫当关，万夫莫开之势。缺点是一技能的强化普攻和解除控制的效果会被浪费。'
# 获取分词
seg_list = jieba.cut(sentence, cut_all=False)
print(' '.join(seg_list))
# 获取分词和词性
words = pseg.cut(sentence)
for word, flag in words:
	print('%s, %s' % (word, flag))


# 通过TF-IDF获取关键词
keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
for item in keywords:
    print(item[0],item[1])
print('-'*100)

# 基于TextRank算法的关键词抽取
#keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n','nr','ns'))
#keywords = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('ns', 'n', 'vn', 'v')) 
#keywords = jieba.analyse.textrank(sentence, topK=20, withWeight=True, allowPOS=('n', 'ns')) 
keywords = jieba.analyse.textrank(sentence, topK=20, withWeight=True) 
print(keywords)
for item in keywords:
    print(item[0],item[1])
