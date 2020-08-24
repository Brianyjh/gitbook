import pandas as pd
import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt, font_manager
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

my_font = font_manager.FontProperties(fname=r"C:\Users\brianyang\AppData\Local\Microsoft\Windows\Fonts\HYJinKaiJ.ttf")

if __name__ == "__main__":
    path = "Advertising.csv"
    data = pd.read_csv(path)
    # data = np.genfromtxt('Advertising.csv', delimiter=',',skip_header=1)
    # print(data)
    x = data.loc[:, ['TV', 'Radio', 'Newspaper']]
    # x = data[:,1]
    y = data['Sales']
    # print(x)
    # print(y)

    # fig = plt.figure(figsize=(20, 8), dpi=80)
    # plt.plot(data['TV'], y,'ro', label='TV')
    # # plt.plot(data['Radio'], y, 'g^', label='Radio')
    # # plt.plot(data['Newspaper'], y, 'mv', label='Newspaer')
    # plt.legend()
    # plt.xlabel('广告花费', fontsize=16, fontproperties=my_font)
    # plt.ylabel('销售额', fontsize=16, fontproperties=my_font)
    # plt.title('广告花费与销售额对比数据', fontsize=20, fontproperties=my_font)
    # plt.grid()
    # plt.show()

    plt.figure(facecolor='w', figsize=(9, 10))
    plt.subplot(311)
    plt.plot(data['TV'], y, 'ro')
    plt.title('TV')
    plt.grid()
    plt.subplot(312)
    plt.plot(data['Radio'], y, 'g^')
    plt.title('Radio')
    plt.grid()
    plt.subplot(313)
    plt.plot(data['Newspaper'], y, 'b*')
    plt.title('Newspaper')
    plt.grid()
    plt.tight_layout()

    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
    # print(x.shape)
    # print(x_train.shape)
    # print(y_train.shape)
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    # print(model)
    print(linreg.coef_)   #线性模型的系数
    print("\n")
    print(linreg.intercept_)  #截距

    order = y_test.argsort(axis=0)
    y_test = y_test.values[order]
    x_test = x_test.values[order, :]
    y_hat = linreg.predict(x_test)
    mse = np.average((y_hat - np.array(y_test)) ** 2)

    # print("hhhhh\n")
    # print(y_test)# 线性模型的系数
    # print("\n")
    # print(order)






    plt.show()
