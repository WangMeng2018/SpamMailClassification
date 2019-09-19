# -*- coding: utf-8 -*-
import codecs
import jieba
from sklearn.externals import joblib
import os
import time

model_path = os.getcwd() + '//experiment//lr_model//'
vectorizer = joblib.load(model_path + 'vectorizer.model')
transformer = joblib.load(model_path + 'transformer.model')
stoplist = codecs.open(model_path + 'stopwords.txt','r',encoding="utf-8").readlines()
stoplist = set(w.strip() for w in stoplist)
lr = joblib.load(model_path +'lr.model')

def preprocess_test(text):
    #加载停用词
    dataSet = []
    segs = list(jieba.cut(text,cut_all=False))
    segs = [word for word in list(segs) if word not in stoplist] #去停用词

    data_cut = segs[0]
    for i in range(1,len(segs)):
        data_cut += ' '+segs[i]
    dataSet.append(data_cut)
    return dataSet


def tfIdf_test(dataSet):
    X = vectorizer.transform(dataSet)
    tfidf = transformer.transform(X)
    return tfidf

def text_test(text):
    print("Start LR Test!")
    start_time = time.time()
    text_pro = preprocess_test(text)
    x = tfIdf_test(text_pro)
    #print(x)
    predict = lr.predict(x)
    end_time = time.time()
    time_result = ("%.3f" % (end_time - start_time))
    print("LR predict result:",predict[0])
    print("LR predict time:",time_result)    
    if predict[0] == '0':
        return "正常信息",time_result
    else:
        return "垃圾信息",time_result

