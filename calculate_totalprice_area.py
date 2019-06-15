"""
    任务：房屋价格预测
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

DATA_FILE = 'csv_to_csv.csv'

# 使用的特征列

FEAT_COLS = ['totalprice','mianji']


def plot_fitting_line(linear_reg_model, X, y, feat):  #画图函数，传入参数：模型，X，y，特征名称
    """
        绘制线型回归线
    """
    w = linear_reg_model.coef_    #模型的一次参数
    b = linear_reg_model.intercept_   #模型截距

    plt.figure()
    # 样本点
    plt.scatter(X, y, alpha=0.5)       #画散点，透明度50%

    # 直线
    plt.plot(X, w * X + b, c='red')      #画线，描点连线，红色线
    plt.title(feat)   #题目
    plt.savefig("北京二手房与面积的房价预测.png")
    plt.show()


def main():
    """
        主函数
    """
    house_data = pd.read_csv(DATA_FILE, usecols=FEAT_COLS,encoding='gbk')

    for feat in FEAT_COLS:
        X = house_data[feat].values.reshape(-1, 1)  
        #house_data[feat].values虽然是一列，但是它会自动转换成行向量，所以要重新塑形成列
        y = house_data['totalprice'].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=10)
        linear_reg_model = LinearRegression()   #模型
        linear_reg_model.fit(X_train, y_train)  #训练
        r2_score = linear_reg_model.score(X_test, y_test)  #R2评分
        print('特征：{}，R2值：{}'.format(feat, r2_score))

        # 绘制拟合直线
        plot_fitting_line(linear_reg_model, X_test, y_test, feat)


if __name__ == '__main__':
    main()