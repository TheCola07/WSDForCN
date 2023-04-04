from gensim.models import Word2Vec
import numpy as np
import jieba
model = Word2Vec.load(r'E:\pyLearn\WSD\Data\corpusSegDone_1.model')

print(model.wv.most_similar(u"放"))

# conten='我把钱放桌子上'                 #试试'我把钱放在桌子上'
# des1='再将采来的嫩茶放太阳下晒'
# des2='把对自己孩子的关心与爱放在最高点'
# des3='这些浓缩铀现在掩埋在瓦砾堆中没有放出任何辐射线'

# content = list(jieba.cut(conten,cut_all=False))
# dest1 = list(jieba.cut(des1,cut_all=False))
# dest2 = list(jieba.cut(des2,cut_all=False))
# dest3 = list(jieba.cut(des3,cut_all=False))

# print(content)
# print(dest1)
# print(dest2)
# print(dest3)

content=['我','把','钱','放','在','桌子', '上']
dest1=['再','将','采来', '的','嫩茶','放','太阳下','晒']
dest2=['把','对','自己', '孩子', '的', '关心', '与', '爱', '放', '在', '最高', '点']
dest3=['这', '些', '浓缩', '铀', '现在', '掩埋', '在', '瓦砾', '堆', '中', '没有', '放', '出', '任何', '辐射', '线']

def w2v_mean(essay,model):
    ls=np.zeros(50)
    for unit in essay:
        try:
            ls+=np.array(model.wv[unit])
        except:
            pass
    return ls/len(essay)

content=w2v_mean(content,model)
d1=w2v_mean(dest1,model)
d2=w2v_mean(dest2,model)
d3=w2v_mean(dest3,model)
print(np.dot(d1,content)/(np.linalg.norm(d1)*(np.linalg.norm(content))))
print(np.dot(d2,content)/(np.linalg.norm(d2)*(np.linalg.norm(content))))
print(np.dot(d3,content)/(np.linalg.norm(d3)*(np.linalg.norm(content))))
