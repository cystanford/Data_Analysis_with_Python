#-*- encoding:utf-8 -*-
from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba

text = '王者荣耀典韦连招是使用一技能+大招+晕眩+二技能+普攻。这套连招主要用于先手强开团，当发现对面走位失误或撤退不及时，我们就可以利用一技能的加速。此外配合大招减速留住对手，协同队友完成击杀。\
当对方站位较集中时，我们同样可以利用“一技能+大招+晕眩”进行团控和吸收伤害。\
在吸收伤害的同时我们还可以利二技能打出不错的输出。这套连招重要的是把握时机，要有一夫当关，万夫莫开之势。\
缺点是一技能的强化普攻和解除控制的效果会被浪费。\
连招二：大招+晕眩+二技能+普攻+一技能+普攻。\
这套连招用于偷袭对手后排很是好用，利用草丛埋伏。\
大招跳到对面身上。迅速晕眩对手，接着二技能继续减速对手，二技能命中后会提升典韦到极限攻速，这时不断普攻，接下来一般会遇到两种情况，当对手继续逃跑时，我们利用一技能加速追击对手，强化普攻击杀对手。\
当对手用技能控住我们我们可以利用一技能解除控制，追击并完成击杀。'

# 输出关键词，设置文本小写，窗口为2
tr4w = TextRank4Keyword()
tr4w.analyze(text=text, lower=True, window=3)
print('关键词：')
for item in tr4w.get_keywords(20, word_min_len=2):
    print(item.word, item.weight)


# 输出重要的句子
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')
print('摘要：')
# 重要性较高的三个句子
for item in tr4s.get_key_sentences(num=3):
	# index是语句在文本中位置，weight表示权重
    print(item.index, item.weight, item.sentence)
