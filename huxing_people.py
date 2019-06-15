import pandas as pd
import matplotlib.pyplot as plt
#导入数值计算库
data = pd.read_csv('csv_to_csv.csv',encoding="GBK")  # 读取训练数据
#去掉房屋面积中「平米」并保存为浮点型
#data = pd.DataFrame((x.split('/') for x in data1['houseinfo']) ,index=data1['houseinfo'].index,columns=['xiaoqu','huxing','mianji','chaoxiang','zhuangxiu','dianti',''])
#导入图表库
#绘制房源户型分布条形图
lis = []
for key in data['huxing'].value_counts():
    lis.append(key)
print(lis)
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
"""
绘制水平条形图方法barh
参数一：y轴
参数二：x轴
"""
plt.figure(figsize=(8,5),dpi=80)
lis = plt.barh(range(len(lis)),lis,height=0.6,color='cyan',alpha=0.7)
plt.yticks(range(len(lis)),data['huxing'].value_counts().index)
plt.xlim(0,2000)
plt.xlabel('人数')
plt.title('户型数量分布')
plt.grid(alpha=0.2)
#编辑文本
for x in lis:
    width = x.get_width()
    plt.text(width+1,x.get_y()+x.get_height()/2,str(width),ha='center',va='center')
plt.savefig('户型人数显示.jpg')
plt.show()
#去掉房屋面积中「平米」并保存为浮点型


