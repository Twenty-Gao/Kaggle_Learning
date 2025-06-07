# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

import pandas as pd

# 假设数据集名为 'titanic.csv'
data = pd.read_csv('sample_submission.csv')

# 查看数据集的前五行
print(data.head())
# 检查缺失值
print(data.isnull().sum())

# 填补缺失值
data['Age'].fillna(data['Age'].median(), inplace=True)

# 删除不必要的列
data.drop(['Ticket', 'Cabin'], axis=1, inplace=True)

# 转换类别变量
data = pd.get_dummies(data, columns=['Sex'], drop_first=True)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
