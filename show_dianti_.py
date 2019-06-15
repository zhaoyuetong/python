from pyecharts import Bar,Pie
import pandas as pd
data = pd.read_csv('csv_to_csv.csv',encoding="GBK")  # 读取训练数据
house_loft= data.groupby(['dianti','region'])['unitprice'].agg(['size','mean','sum']).round(0).reset_index()
house_loft.columns=['有无电梯','所在区','数量','单价','总价之和']
print (house_loft)
#value=data[u'有无电梯'].groupby(data[u'所在区']).size().round(0).tolist()
#print (value)
#print (name)

pie = Pie("北京二手房有无电梯房源数量(套)",width=700,height=400,)
pie.add("", ['有电梯','无电梯'],[house_loft[house_loft['有无电梯']=='有电梯']['数量'].sum(),house_loft[house_loft['有无电梯']=='无电梯']['数量'].sum()],is_label_show=True,is_toolbox_show=False,label_formatter='{b}:{c},{d}%')
pie.show_config()
pie.render('北京二手房有无电梯房源数量.html')

bar=Bar('北京各区二手房有无电梯房源数量',width=900)
bar.add('有电梯',house_loft[house_loft['有无电梯']=='有电梯']['所在区'],house_loft[house_loft['有无电梯']=='有电梯']['数量'],is_label_show=True,label_text_color='#000',label_pos='inside',is_stack=True)
bar.add('无电梯',house_loft[house_loft['有无电梯']=='无电梯']['所在区'],house_loft[house_loft['有无电梯']=='无电梯']['数量'],is_label_show=True,is_stack=True)
bar.show_config()
bar.render('北京各区二手房有无电梯房源数量.html')

bar=Bar('北京各区有无电梯二手房平均单价(元/平米)',width=900)
bar.add('有电梯',house_loft[house_loft['有无电梯']=='有电梯']['所在区'],house_loft[house_loft['有无电梯']=='有电梯']['单价'],is_label_show=True,mark_line=['average'],is_toolbox_show=False)
bar.add('无电梯',house_loft[house_loft['有无电梯']=='无电梯']['所在区'],house_loft[house_loft['有无电梯']=='无电梯']['单价'],is_label_show=True,mark_line=['average'],is_toolbox_show=False)
bar.show_config()
bar.render('北京各区有无电梯二手房平均单价.html')