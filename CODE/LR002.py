# coding:utf-8

import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split, GridSearchCV
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

if __name__ == "__main__":
    data = pd.read_csv('Advertising.csv')
    x = data[['TV', 'Radio', 'Newspaper']]
    y = data['Sales']

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    model = Lasso()
    alpha_can = np.logspace(-3, 2, 10)
    np.set_printoptions(suppress=True)
    print('alpha_can = ', alpha_can)
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)  # 暴力调参，五折交叉验证
    lasso_model.fit(x_train, y_train)
    print("超参数：\n", lasso_model.best_params_)

    order = y_test.argsort()
    y_test = y_test.values[order]
    x_test = x_test.values[order, :]
    y_hat = lasso_model.predict(x_test)
    print(lasso_model.score(x_test, y_test))
    mse = np.average((y_hat - np.array(y_test)) ** 2)
    rmse = np.sqrt(mse)
    print(mse, rmse)

    t = np.arange(len(x_test))
    mpl.rcParams['font.sans-serif'] = ['simHei']  # 用来正常显示中文标签
    mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.figure(facecolor='w')
    plt.plot(t, y_test, 'r-', linewidth=2, label='真实数据')
    plt.plot(t, y_hat, 'g-', linewidth=2, label='预测数据')
    plt.title('线性回归预测销量', fontsize=18)
    plt.legend(loc='lower right')
    plt.grid()
    plt.show()
