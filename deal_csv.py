# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:18:30 2019
@author: Administrator
"""
import shutil
#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory
import glob
import time
import csv, os
#这里是将生成的各个区域的csv合并成一个csv，其实就是拷贝到removeCsvHeader文件下然后删除除lianjiawangchangping.csv之外的各区表头，最后删除removeCsvHeader文件
os.makedirs('headerRemoved', exist_ok=True)
# Loop through every file in the current working directory.
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue
    print('Removing header from ' + csvFilename + '...')
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        print(row)
        if readerObj.line_num == 1 and csvFilename!='lianjiawangchangping.csv':
            continue	# skip first row
        csvRows.append(row)
    csvFileObj.close()
	# Write out the CSV file.
    if csvFilename!='csv_to_csv.csv':
        csvFileObj  = open(os.path.join('headerRemoved', csvFilename), 'w', 
					newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
csvx_list = glob.glob('headerRemoved'+'/'+'*.csv')
print('总共发现%s个CSV文件'% len(csvx_list))
time.sleep(2)
print('正在处理............')
for i in csvx_list:
    fr = open(i,'r').read()
    with open('csv_to_csv.csv','a') as f:
        f.write(fr)
    print('写入成功！')
print('写入完毕！')
print('5秒钟自动关闭程序！')
time.sleep(5)
dir = 'headerRemoved'
shutil.rmtree(dir)