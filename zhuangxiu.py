from pyecharts import Bar,Pie
import pandas as pd
data = pd.read_csv('csv_to_csv.csv',encoding="GBK")  # 读取训练数据
house_loft= data.groupby(['zhuangxiu','region'])['unitprice'].agg(['size','mean','sum']).round(0).reset_index()
house_loft.columns=['装修','所在区','数量','单价','总价之和']
print (house_loft)
#value=data[u'有无电梯'].groupby(data[u'所在区']).size().round(0).tolist()
#print (value)
#print (name)

pie = Pie("北京二手房装修房源数量(套)",width=700,height=400,)
pie.add("", fit_up_price['装修'],fit_up_price['计数'],is_label_show=True,legend_orient="vertical",legend_pos="right",is_toolbox_show=False,label_formatter='{b}:{c},{d}%')
pie.show_config()
pie.render('北京二手房装修房源数量.html')
bar.use_theme("macarons")
bar=Bar('北京各区二手房装修房源数量(套)',width=900)
bar.add('精装',house_fitup[house_fitup['装修']=='精装']['所在区'],house_fitup[house_fitup['装修']=='精装']['数量'],is_label_show=True,label_text_color='#000',label_pos='inside',is_stack=True)
bar.add('简装',house_fitup[house_fitup['装修']=='简装']['所在区'],house_fitup[house_fitup['装修']=='简装']['数量'],is_label_show=True,label_text_color='#000',label_pos='inside',is_stack=True)
bar.add('毛坯',house_fitup[house_fitup['装修']=='毛坯']['所在区'],house_fitup[house_fitup['装修']=='毛坯']['数量'],is_label_show=True,is_stack=True)

bar.show_config()
bar.render('北京各区二手房装修房源数量.html')
bar.use_theme("macarons")
bar=Bar('北京各区装修二手房平均单价(元/平米)',width=900)
bar.add('精装',house_fitup[house_fitup['装修']=='精装']['所在区'],house_fitup[house_fitup['装修']=='精装']['单价'],is_label_show=True,label_text_color='#000',bar_category_gap='30%',mark_line=['average'],is_toolbox_show=False)
bar.add('简装',house_fitup[house_fitup['装修']=='简装']['所在区'],house_fitup[house_fitup['装修']=='简装']['单价'],is_label_show=True,label_text_color='#000',label_pos='inside',bar_category_gap='30%',mark_line=['average'],is_toolbox_show=False)
bar.add('毛坯',house_fitup[house_fitup['装修']=='毛坯']['所在区'],house_fitup[house_fitup['装修']=='毛坯']['单价'],is_label_show=True,label_text_color='#000',bar_category_gap='30%')

bar.show_config()
bar.render('北京各区装修二手房平均单价.html')