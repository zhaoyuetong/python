import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl 
#导入数值计算库
from sklearn.linear_model import LinearRegression
house = pd.read_csv('csv_to_csv.csv',encoding="GBK")  # 读取训练数据
#分析个城市二手房价格
#指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
#获取总价格全五的数据
# 将字符串转换成数字主要用于处理面积的数据
def data_adj(area_data, str):
    #判断‘平米’在不在这个数据里
    if str in area_data : 
        #用find()函数查找字符串的索引位置，方便截取  
        return float(area_data[0:area_data.find(str)]) 
    else : return None
#
#house['mianji'][3622] = float(house['mianji'][3622].replace('3室2厅','66.76'))
#house['mianji'][3626] = float(house['mianji'][3626].replace('4室2厅','66.76'))

#print(house['mianji'])
#计算户型的所占的个数，用到value_counts(),排序也给你做好了，你可以清楚的看到所占的个数
housetype = house['huxing'].value_counts()

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
#设置画布
asd,sdf = plt.subplots(1,1,dpi=100) #获取前10条数据
housetype.head(5).plot(kind='bar',x='huxing',y='size',title='户型数量分布',ax=sdf) 
plt.legend(['数量']) 
plt.savefig('户型数量分布.jpg')
plt.show()
#print(house['guanzhu'].str.replace('人关注',''))
#户型和关注人数分布
type_interest_group = house['guanzhu'].groupby(house['huxing']).agg([('户型', 'count'), ('关注人数', 'sum')])
#print(house['guanzhu'].str.replace('人关注','').values)
#获取户型数量大于50 的数据
ti_sort = type_interest_group[type_interest_group['户型'] > 50 ].sort_values(by='户型')
#画图
#print(ti_sort)
asd,sdf = plt.subplots(1,1,dpi=150) 
ti_sort.plot(kind='barh',alpha=0.7,grid=True,ax=sdf)
plt.title('二手房户型和关注人数分布')
plt.ylabel('户型') 
plt.savefig('二手房户型和关注人数分布.jpg')
plt.show()


#户型和看房次数数分布
type_interest_num = house['daikan'].groupby(house['huxing']).agg([('户型', 'count'), ('看房次数', 'sum')])
ti_sort = type_interest_num[type_interest_num['户型'] > 50 ].sort_values(by='户型')
#画图
asd,sdf = plt.subplots(1,1,dpi=150)
ti_sort.plot(kind='barh',alpha=0.7,grid=True,ax=sdf)
plt.title('二手房户型和看房次数')
plt.ylabel('户型') 
plt.savefig('二手房户型和看房次数.jpg')
plt.show()


area_level = [0, 50, 100, 150, 200, 250, 300, 500] 
label_level = ['小于50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']
#算出所面积在哪个区间
house['mianji'] = house['mianji'].astype(float)
are_cut = pd.cut(house['mianji'],area_level,label_level)
#计算面积在所设置的区间的数量
acreage = are_cut.value_counts()
asd,sdf = plt.subplots(1,1,dpi=150)
acreage.plot(kind='bar',rot=30,alpha=0.4,grid=True,ax=sdf)
plt.title('二手房面积分布')    
plt.xlabel('面积')    
plt.legend(['数量']) 
plt.savefig('二手房面积分布.jpg')   
plt.show()


#各个区房源均价
region =house.groupby('region').mean()['unitprice']

asd,sdf = plt.subplots(1,1,dpi=150)
region.plot(kind='bar',x='region',y='unitprice', title='各个区域房源均价',ax=sdf)
plt.savefig('各个区域房源均价.jpg')
plt.show()

#各个区域房源数量排序
region_num = house.groupby('region').size().sort_values(ascending=False)

region_num = house.groupby('region').size().sort_values(ascending=False) 
asd,sdf = plt.subplots(1,1,dpi=150) 
region_num.plot(kind='bar',x='region',y='size',title='各个区域房源数量分布',ax=sdf) 
plt.legend(['数量']) 
plt.savefig('各个区域房源数量分布.jpg')
plt.show()

#北京在售面积最小二手房
house.sort_values('mianji').iloc[0,:]

# 各个区域小区房源数量
community_num =house.groupby('xiaoqu').size().sort_values(ascending=False) #画图
asd,sdf = plt.subplots(1,1,dpi=150) #取前十五个
community_num.head(15).plot(kind='bar',x='xiaoqu',y='size',title='各个区域小区房源数量',ax=sdf)
plt.legend(['数量']) 
plt.savefig('各个区域小区房源数量.jpg')
plt.show()

#各个小区的房源均价
community_mean = house.groupby('xiaoqu').mean()['unitprice'].sort_values(ascending=False) #画图
asd,sdf = plt.subplots(1,1,dpi=150) #前10 条
community_mean.head(10).plot(kind='bar',x='community',y='mean',title='各个小区房源均价',ax=sdf) 
plt.legend(['均价']) 
plt.savefig('各个小区房源均价.jpg')
plt.show()

#个个小区看房人数
community_fsum = house['daikan'].groupby(house['xiaoqu']).agg([('小区', 'count'), ('看房次数', 'sum')]) 
commnuity_count = community_fsum[community_fsum['小区'] >15].sort_values(by='小区') #画图
asd,sdf = plt.subplots(1,1,dpi=150) 
commnuity_count.plot(kind='barh',ax=sdf) 
plt.title('各个小区看房人数') 
plt.savefig('各个小区看房人数.jpg')
plt.show()

#绘制面积和总价的散点图
data1 = house[house["mianji"] <= 300] #筛选面积小于300
area = data1[["mianji"]]
totalprice = data1[["totalprice"]]
plt.scatter(area, totalprice)
plt.title('北京市总价与面积分布散点图')
plt.show


#使用单元线性回归拟合
linear = LinearRegression()
model = linear.fit(area, totalprice)

#预测房价对应的面积
price = model.predict(area)
#将预测的房价和散点图绘制在一张图上
#根据面积预测出相应的价格
#plt.figure(figsize=(20,10))
area = data1[["mianji"]]
totalprice = data1[["totalprice"]]
plt.scatter(area, totalprice)
plt.plot(area, price, color="DeepPink")
plt.title('北京市二手房价预测')

plt.show()