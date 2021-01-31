# -*- coding: utf-8 -*-
"""WordOccurancesDemo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P6IMvNtxrpvRCsc9-E3bvBMkFRGvBTRT
"""

# tokenization and Part-Of-Speech tagging 
import jieba
import jieba.posseg as pseg

strs = ["你想他的父母会不会知道他偷钱？","会不会称赞他？"]

for str in strs:
  seg_list = jieba.cut(str, cut_all=True)
  print("Full Mode: " + "/ ".join(seg_list))

words = pseg.cut("会不会称赞他")
jieba.enable_paddle()
words = pseg.cut("会不会称赞他",use_paddle=True)
for word,flag in words:
  print('%s %s'%(word,flag))
