from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from experiment.lr_model import lr_model
from experiment.lgbm_model.code import predict as lgbm_predict
from experiment.svm_model import SVM as svm_predict
from experiment.dt_model import dt_model as dt_predict

def index(request):

    if request.method == 'GET':
        return render(request, 'index.html')

    if request.method == 'POST':
        message_text = request.POST.get('pmessage')
        algor_list = request.POST.getlist('Algor')
        print(message_text,algor_list)
        # 算法处理过程
        classify_result = []
        if request.POST.get('pmessage') == '':
            return render(request, 'index.html', {'data':classify_result})

        if algor_list[0] == '0':
            algor_list = ['1','2','3','4']
        for algor_no in algor_list:
            if algor_no == '1':
                svm_result,svm_time = svm_predict.svm_test(message_text)
                tmp = {'name':'SVM','answer':svm_result,'time':str(svm_time) + 's'}
                #tmp = {'name':'SVM','answer':'正常信息','time':'2.29s'}
                classify_result.append(tmp)
            if algor_no == '2':
                lr_result,time_result = lr_model.text_test(message_text)
                tmp = {'name':'LR','answer':lr_result,'time':str(time_result) + 's'}
                classify_result.append(tmp)
            if algor_no == '3':
                dt_result,time_result = dt_predict.dt_test(message_text)
                tmp = {'name':'决策树','answer':dt_result,'time':str(time_result) + 's'}
                classify_result.append(tmp)
            if algor_no == '4':
                lgbm_result,lgbm_time = lgbm_predict.lgbm_test(message_text)
                tmp = {'name':'Boosting','answer':lgbm_result,'time':str(lgbm_time) + 's'}             
                classify_result.append(tmp)
        return render(request, 'index.html', {'data':classify_result})
