import numpy as np
import jieba
import jieba.posseg as pseg
import sklearn.feature_extraction.text
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.externals import joblib
from time import time
from scipy import sparse, io
import json
import re
import os


class MessageCountVectorizer(sklearn.feature_extraction.text.CountVectorizer):
    def build_analyzer(self):
        def analyzer(doc):
            words = pseg.cut(doc)
            new_doc = ''.join(w.word for w in words if w.flag != 'x')
            words = jieba.cut(new_doc)
            return words
        return analyzer

model_path = os.getcwd() + '//experiment//dt_model//'
# 加载特征
feature_path = model_path + 'feature.pkl'
loaded_vec = MessageCountVectorizer(decode_error="replace", vocabulary=joblib.load(open(feature_path, "rb")))
# 加载TfidfTransformer
tfidftransformer_path = model_path + 'tfidftransformer.pkl'
tfidftransformer = joblib.load(open(tfidftransformer_path, "rb"))
#加载模型  
clf = joblib.load(model_path + 'decision_tree.pkl') 

#if '__main__' == __name__:
def dt_test(text):
  print("Start SVM Test!")
  #text = '感谢致电杭州萧山全金釜韩国烧烤店，本店位于金城路xxx号。韩式烧烤等，价格实惠、欢迎惠顾,全金釜韩国烧烤店'
  content = []
  content.append(text)
  t0 = time()
  count_vector=loaded_vec.transform(content)
  data_tfidf = tfidftransformer.transform(count_vector) 
  #预测结果（0为正常短信，1为垃圾短信）
  result = clf.predict(data_tfidf)
  run_result = result[0]
  run_time = ("%.3f" % (time() - t0))
  print("DT predict result:",run_result)
  print("DT predict time:",run_time)
  if run_result == '0':
      return "正常信息",run_time
  else:
      return "垃圾信息",run_time

