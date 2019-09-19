import os

svm_res_path = 'E://WebDataMining//unlabel_data//svm_result.txt'
lr_res_path = 'E://WebDataMining//unlabel_data//lr_result.txt'
lgbm_res_path = 'E://WebDataMining//unlabel_data//lgbm_result.txt'
dt_res_path = 'E://WebDataMining//unlabel_data//dt_result.txt'
all_path = 'E://WebDataMining//unlabel_data//all_result.txt'

lr_list = []
svm_list = []
lgbm_list = []
dt_list = []
data_list = []

lgbm_file = open(lgbm_res_path,'r', encoding='UTF-8')
lines = lgbm_file.readlines()
for line in lines: 
    d = line.strip('\n').split('\t')
    lgbm_list.append(int(d[1]))
    data_list.append(d[2])
lgbm_file.close()

lr_file = open(lr_res_path,'r', encoding='UTF-8')
lines = lr_file.readlines()
for line in lines: 
    d = line.strip('\n').split(' ')
    lr_list.append(int(d[1]))
lr_file.close()

dt_file = open(dt_res_path,'r', encoding='UTF-8')
lines = dt_file.readlines()
for line in lines: 
    d = line.strip('\n')
    dt_list.append(int(d[0]))
dt_file.close()

svm_file = open(svm_res_path,'r', encoding='UTF-8')
lines = svm_file.readlines()
for line in lines: 
    d = line.strip('\n').split('\t')
    svm_list.append(int(d[1]))
svm_file.close()

w = open(all_path,'w', encoding='UTF-8')
for i in range(len(lgbm_list)):
	w.write(str(i+1) + '\t' + str(svm_list[i]) + '\t' + str(lr_list[i]) + '\t' + str(dt_list[i]) + '\t' + str(lgbm_list[i]) + '\t' + data_list[i] + '\n')
w.close()
