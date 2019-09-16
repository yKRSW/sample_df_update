# -*- coding: utf-8 -*-
"""
@author : yKRSW
@purpose: Sample of updating DataFrame
"""

# Initialize
import pandas as pd
import numpy as np

cols = ["x1", "x2", "y"]
vals = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
df = pd.DataFrame(vals, columns=cols)
print(df)

#    x1  x2   y
# 0   1   2   3
# 1   4   5   6
# 2   7   8   9
# 3  10  11  12

print()

# split data
df_train, df_test = df.iloc[0:-2], df.iloc[-2:]
print(df_train)
#    x1  x2  y
# 0   1   2  3
# 1   4   5  6

print(df_test)
#    x1  x2   y
# 2   7   8   9
# 3  10  11  12

print()

# add new column
y_pred_train = [3.1, 6.2]
df_train = df_train.assign(y_pred = y_pred_train)
y_pred_test = [9.3, 12.4]
df_test = df_test.assign(y_pred = y_pred_test)

print(df_train)
#    x1  x2  y  y_pred
# 0   1   2  3     3.1
# 1   4   5  6     6.2

print(df_test)
#    x1  x2   y  y_pred
# 2   7   8   9     9.3
# 3  10  11  12    12.4

print()

# concat split data to original (Override)
df1 = df.copy()
df1["y_pred"] = df_train["y_pred"]
df1["y_pred"] = df_test["y_pred"]
print(df1)

#    x1  x2   y  y_pred
# 0   1   2   3     NaN
# 1   4   5   6     NaN
# 2   7   8   9     9.3
# 3  10  11  12    12.4

print()

# concat split data to original (Lack of column)
df2 = df.copy()
df2.update(df_train)
df2.update(df_test)
print(df2)

#      x1    x2     y
# 0   1.0   2.0   3.0
# 1   4.0   5.0   6.0
# 2   7.0   8.0   9.0
# 3  10.0  11.0  12.0

print()

# concat split data to original (Update)
df3 = df.copy()
df3["y_pred"] = None
df3.update(df_train)
df3.update(df_test)
print(df3)

#      x1    x2     y y_pred
# 0   1.0   2.0   3.0    3.1
# 1   4.0   5.0   6.0    6.2
# 2   7.0   8.0   9.0    9.3
# 3  10.0  11.0  12.0   12.4

print()
