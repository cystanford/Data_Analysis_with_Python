# -*- coding:utf-8 -*-
# 生成词云
from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from lxml import etree
from nltk.tokenize import word_tokenize

# 去掉停用词
def remove_stop_words(f):
	stop_words = ['nan']
	for stop_word in stop_words:
		f = f.replace(stop_word, '')
	return f

# 生成词云
def create_word_cloud(f):
	print('根据词频，开始生成词云!')
	f = remove_stop_words(f)
	cut_text = word_tokenize(f)
	#print(cut_text)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	# 写词云图片
	wordcloud.to_file("wordcloud.jpg")
	# 显示词云文件
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

# 数据加载
data = pd.read_csv('./Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, data.shape[0]):
    transactions.append([str(data.values[i, j]) for j in range(0, 20)])

all_word = " ".join('%s' %id for id in transactions)
#print(all_word)
# 生成词云
create_word_cloud(all_word)
