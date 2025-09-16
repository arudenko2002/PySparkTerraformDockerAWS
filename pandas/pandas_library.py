import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame({'A': [1, 2, 3]})
print("pd.DataFrame({'A': [1, 2, 3]}) =\n", data)
# pd.DataFrame({'A': [1, 2, 3]}) =
#     A
# 0  1
# 1  2
# 2  3
#Object Creation
data = pd.Series([1, 3, 5, np.nan, 6, 8])
print("data = pd.Series([1, 3, 5, np.nan, 6, 8]) =\n", data)
# data = pd.Series([1, 3, 5, np.nan, 6, 8]) =
#  0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0

dates = pd.date_range("20130101", periods=6)
print('pd.date_range("20130101", periods=6) =\n', dates)
# pd.date_range("20130101", periods=6) =
#  DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print('pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) =\n', df)
# pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD")) =
#                     A         B         C         D
# 2013-01-01 -0.067344  0.839264  0.701111 -0.724853
# 2013-01-02 -0.055438  0.528045  0.526078 -0.281371
# 2013-01-03  0.354941  0.375253 -0.247457 -1.155704
# 2013-01-04 -0.916493  0.716704 -1.287190  0.752271
# 2013-01-05 -1.194067  0.840385  0.733555  0.212677
# 2013-01-06 -0.252798 -0.735272 -0.171934  0.853234

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo

print(df2.dtypes)
# A          float64
# B    datetime64[s]
# C          float32
# D            int32
# E         category
# F           object
# dtype: object
# ViewingData
def viewing_data():
    print(df2.head(3)) #default=5
    #      A          B    C  D      E    F
    # 0  1.0 2013-01-02  1.0  3   test  foo
    # 1  1.0 2013-01-02  1.0  3  train  foo
    # 2  1.0 2013-01-02  1.0  3   test  foo

    print(df2.tail(2))
    #      A          B    C  D      E    F
    # 2  1.0 2013-01-02  1.0  3   test  foo
    # 3  1.0 2013-01-02  1.0  3  train  foo

    print(df2.index)
    # Index([0, 1, 2, 3], dtype='int64')

    print(df2.columns)
    # Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')

    print(df)
    #                    A         B         C         D
    # 2013-01-01 -0.212862 -0.344171 -0.230295  0.684608
    # 2013-01-02 -0.589206 -1.219877 -1.297611  0.233334
    # 2013-01-03  2.018922 -0.327043  0.835531  0.633800
    # 2013-01-04 -0.999965  0.506898  2.074518  0.281780
    # 2013-01-05  0.567126  0.801771 -0.463059 -0.977140
    # 2013-01-06  1.103757  1.064173  0.223107  1.843754
    data = df.to_numpy()
    print(data)
    # [[-1.50598049  0.65712945  2.38657993  2.19432947]
    #  [-1.49728428 -0.9001955   0.17827166  1.02219325]
    #  [-0.42086674  2.08912639 -0.39690564 -0.43255099]
    #  [-0.20558214 -0.50788931 -1.24916007 -0.44968704]
    #  [ 1.52299931  0.24256285  1.0350202   0.95958306]
    #  [-0.6990839   0.22262178  1.96236828  0.05368209]]

    print(df.describe)
    # <bound method NDFrame.describe of                    A         B         C         D
    # 2013-01-01 -0.048133 -0.789068  0.160863 -0.735412
    # 2013-01-02 -1.873961 -0.043686  0.791631 -0.863388
    # 2013-01-03  0.388040  0.088104 -0.906095 -0.775832
    # 2013-01-04  0.269869 -0.054387  1.126093  0.311451
    # 2013-01-05  2.202575  0.334006  0.327645 -2.241226
    # 2013-01-06 -1.757613 -0.764590  1.423038  1.260110>
    print(df.T)
    #    2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
    # A    0.916859    0.598064   -0.494323   -0.102475    0.859294   -0.080846
    # B   -1.598142   -0.995351   -0.259935    0.352883    0.916240    1.602187
    # C    1.350653    0.557041   -0.164342    0.356822    1.446286   -0.279491
    # D    0.184808    1.260425   -1.447602    0.290547    0.111370    1.237821
    data = df.sort_index(axis=1, ascending=False)
    print(data)
    #                    D         C         B         A
    # 2013-01-01 -0.621972 -1.253296  0.286254 -0.065325
    # 2013-01-02  0.012239 -0.111766 -0.649856 -0.742614
    # 2013-01-03  1.412555  2.192706 -0.193661 -0.738952
    # 2013-01-04  0.508601 -0.466790 -0.779990  0.139590
    # 2013-01-05 -0.734496  1.106393  0.958588 -0.422472
    # 2013-01-06  0.604475  0.738955 -1.134947 -2.179076
    data = df.sort_values(by="B")
    print(data)
    #                    A         B         C         D
    # 2013-01-05  0.795740 -0.105655  1.791784 -0.690026
    # 2013-01-02  0.258620 -0.097319  0.458271 -0.021420
    # 2013-01-01 -3.117455  0.334377 -1.212299 -1.784242
    # 2013-01-06 -0.293501  0.516541  0.977873 -1.291527
    # 2013-01-04 -0.612098  0.820096  0.519954 -0.278151
    # 2013-01-03 -1.765754  0.986119 -0.304220 -1.698453

viewing_data()
#Selection
def get_item():
    data = df["A"]
    print(data)
    # 2013-01-01   -0.614183
    # 2013-01-02   -0.337318
    # 2013-01-03    1.936703
    # 2013-01-04    0.349919
    # 2013-01-05    0.428479
    # 2013-01-06    0.022464
    data = df[0:3]
    print(data)
    #                    A         B         C         D
    # 2013-01-01  0.340055 -0.498823  1.467836  1.210291
    # 2013-01-02 -2.130134 -0.324368  1.278388  0.393718
    # 2013-01-03 -0.311360 -1.137088  0.495621 -1.625192
    data = df["20130102":"20130104"]
    print(data)
    #                    A         B         C         D
    # 2013-01-02 -2.130134 -0.324368  1.278388  0.393718
    # 2013-01-03 -0.311360 -1.137088  0.495621 -1.625192
    # 2013-01-04  0.819918 -0.512746  1.643389  1.436887

get_item()

def selection_by_label():
    data = df.loc[dates[0]]
    print(data)
    # A    1.239430
    # B    0.133408
    # C    0.811125
    # D   -0.723663
    # Name: 2013-01-01 00:00:00, dtype: float64
    # Selecting all rows (:) with a select column labels:
    data = df.loc[:,['A', 'B']]
    print(data)
    #                    A         B
    # 2013-01-01  1.239430  0.133408
    # 2013-01-02  0.978724  0.705989
    # 2013-01-03  0.576842 -1.131715
    # 2013-01-04  0.635759  0.122797
    # 2013-01-05  0.485119  0.004791
    # 2013-01-06  0.626649  0.793247
    data = df.loc["20130102":"20130104", ["A", "B"]]
    print(data)
    #                    A         B
    # 2013-01-02  1.212112 -0.173215
    # 2013-01-03 -0.861849 -2.104569
    # 2013-01-04  0.721555 -0.706771
    data = df.loc[dates[0], "A"]
    print(data)
    # 0.5031329286788201
    print(df)
    #                    A         B         C         D
    # 2013-01-01 -0.446006  0.419668 -1.798042  0.160074
    # 2013-01-02  0.513935  0.340075 -0.157948 -0.663463
    # 2013-01-03 -0.361824  0.167874  0.344697 -1.624414
    # 2013-01-04 -0.972985 -0.137640  1.109633 -0.449546
    # 2013-01-05 -0.014349  0.624570  0.466318  0.384265
    # 2013-01-06 -0.414192  1.147240 -0.263262  0.715054

selection_by_label()

def selection_by_position():
    print(df.iloc[3])
    # A   -0.972985
    # B   -0.137640
    # C    1.109633
    # D   -0.449546
    print(df.iloc[3:5, 0:2])
    #                    A        B
    # 2013-01-04 -0.972985 -0.13764
    # 2013-01-05 -0.014349  0.62457
    print(df.iloc[[1, 2, 4], [0, 2]])
    #                    A         C
    # 2013-01-02  0.513935 -0.157948
    # 2013-01-03 -0.361824  0.344697
    # 2013-01-05 -0.014349  0.466318
    print(df.iloc[1:3, :])
    #                    A         B         C         D
    # 2013-01-02  0.513935  0.340075 -0.157948 -0.663463
    # 2013-01-03 -0.361824  0.167874  0.344697 -1.624414
    print(df.iloc[:, 1:3])
    #                    B         C
    # 2013-01-01  0.419668 -1.798042
    # 2013-01-02  0.340075 -0.157948
    # 2013-01-03  0.167874  0.344697
    # 2013-01-04 -0.137640  1.109633
    # 2013-01-05  0.624570  0.466318
    # 2013-01-06  1.147240 -0.263262
    print(df.iloc[1, 1])
    # 0.34007527664635434
    print(df.iat[1, 1])
    # 0.34007527664635434

selection_by_position()

def boolean_indexing():
    print(df[df["A"] > 0])
    #                    A         B         C         D
    # 2013-01-01  0.504168  0.153738 -0.245261  1.797801
    # 2013-01-04  0.776493 -0.342969  2.203712 -0.175322
    # 2013-01-05  0.104610 -1.417657  1.005952  0.326603
    print(df[df > 0])
    #                    A         B         C         D
    # 2013-01-01  0.504168  0.153738       NaN  1.797801
    # 2013-01-02       NaN  0.841469  0.327494  0.354180
    # 2013-01-03       NaN  0.560190  0.275134       NaN
    # 2013-01-04  0.776493       NaN  2.203712       NaN
    # 2013-01-05  0.104610       NaN  1.005952  0.326603
    # 2013-01-06       NaN  0.643802  1.132393       NaN
    df2 = df.copy()
    df2["E"] = ["one", "one", "two", "three", "four", "three"]
    print(df2)
    #                    A         B         C         D      E
    # 2013-01-01  0.085282  0.105270  0.674141  0.889825    one
    # 2013-01-02 -1.478946  0.885290 -1.726990 -0.580994    one
    # 2013-01-03  1.915233  1.361376  0.554623 -1.766895    two
    # 2013-01-04 -0.763378 -1.335413  1.344425 -0.604333  three
    # 2013-01-05  0.495784 -1.181039 -0.046524 -0.221739   four
    # 2013-01-06  0.690838  0.667585  1.758562  0.044070  three
    data = df2[df2["E"].isin(["two", "four"])]
    print(data)
    #                    A         B         C         D     E
    # 2013-01-03  1.915233  1.361376  0.554623 -1.766895   two
    # 2013-01-05  0.495784 -1.181039 -0.046524 -0.221739  four

boolean_indexing()

#Setting
def setting():
    s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))
    print(s1)
    # 2013-01-02    1
    # 2013-01-03    2
    # 2013-01-04    3
    # 2013-01-05    4
    # 2013-01-06    5
    # 2013-01-07    6
    # Freq: D, dtype: int64
    df["F"] = s1
    print(df)
    #                    A         B         C         D    F
    # 2013-01-01 -0.776160 -0.224408 -1.593724  1.238881  NaN
    # 2013-01-02  0.871601  0.514441  1.675812  1.112656  1.0
    # 2013-01-03  0.820290 -0.813864  0.312808  0.075170  2.0
    # 2013-01-04 -0.822670  1.230374 -0.005083 -0.278178  3.0
    # 2013-01-05  1.297831 -1.601174 -1.254256 -0.985783  4.0
    # 2013-01-06  0.432443  0.653766  0.015899  1.113744  5.0
    df.at[dates[0], "A"] = 0
    print(df)
    #                    A         B         C         D    F
    # 2013-01-01  0.000000  1.545176  0.002657  1.500827  NaN
    # 2013-01-02  1.676464  0.585041 -0.567267  0.627566  1.0
    # 2013-01-03  0.277616 -1.315264  0.070518 -0.914148  2.0
    # 2013-01-04  0.098804  0.564849 -1.829850  1.106922  3.0
    # 2013-01-05  0.939278  1.945662  0.057960  1.351614  4.0
    # 2013-01-06  0.797668 -1.794122 -0.553650  0.163885  5.0
    df.iat[0, 1] = 0
    print(df)
    #                    A         B         C         D    F
    # 2013-01-01  0.000000  0.000000  2.357688  0.496607  NaN
    # 2013-01-02  0.251734 -0.640579 -0.374798 -1.639183  1.0
    # 2013-01-03 -0.380164 -0.995485 -1.827273 -3.096382  2.0
    # 2013-01-04 -0.303656 -1.348099 -0.878771 -0.644711  3.0
    # 2013-01-05 -2.342585  1.655595 -0.526710  0.702113  4.0
    # 2013-01-06  0.113065 -0.230205  0.879021 -1.171588  5.0
    df.loc[:, "D"] = np.array([5] * len(df))
    print(df)
    #                    A         B         C    D    F
    # 2013-01-01  0.000000  0.000000  2.357688  5.0  NaN
    # 2013-01-02  0.251734 -0.640579 -0.374798  5.0  1.0
    # 2013-01-03 -0.380164 -0.995485 -1.827273  5.0  2.0
    # 2013-01-04 -0.303656 -1.348099 -0.878771  5.0  3.0
    # 2013-01-05 -2.342585  1.655595 -0.526710  5.0  4.0
    # 2013-01-06  0.113065 -0.230205  0.879021  5.0  5.0
    df2 = df.copy()
    df2[df2 > 0] = -df2
    print(df2)
    #                    A         B         C    D    F
    # 2013-01-01  0.000000  0.000000 -1.509059 -5.0  NaN
    # 2013-01-02 -1.212112 -0.173215 -0.119209 -5.0 -1.0
    # 2013-01-03 -0.861849 -2.104569 -0.494929 -5.0 -2.0
    # 2013-01-04 -0.721555 -0.706771 -1.039575 -5.0 -3.0
    # 2013-01-05 -0.424972 -0.567020 -0.276232 -5.0 -4.0
    # 2013-01-06 -0.673690 -0.113648 -1.478427 -5.0 -5.0

setting()

def missing_data():
    print("AAAAAAAAAA")
    df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
    print(df1)
    #                    A         B         C    D    F   E
    # 2013-01-01  0.000000  0.000000  1.000942  5.0  NaN NaN
    # 2013-01-02  1.021225  0.590646  1.025253  5.0  1.0 NaN
    # 2013-01-03 -0.113823  0.000807 -0.256247  5.0  2.0 NaN
    # 2013-01-04  1.586299  0.293922  0.183469  5.0  3.0 NaN
    df1.loc[dates[0] : dates[1], "E"] = 1
    print(df1)
    #                    A         B         C    D    F    E
    # 2013-01-01  0.000000  0.000000  0.609693  5.0  NaN  1.0
    # 2013-01-02  0.851869  0.962829  0.449798  5.0  1.0  1.0
    # 2013-01-03  0.523858  0.426518  1.774167  5.0  2.0  NaN
    # 2013-01-04  0.022128  2.684758  1.041568  5.0  3.0  NaN
    data = df1.dropna(how="any")
    print(data)
    #                    A        B         C    D    F    E
    # 2013-01-02 -1.207087 -0.36042  0.579986  5.0  1.0  1.0
    data = df1.fillna(value=5)
    print(data)
    #                    A         B         C    D    F    E
    # 2013-01-01  0.000000  0.000000  1.854734  5.0  5.0  1.0
    # 2013-01-02 -0.185308  0.431159 -0.350343  5.0  1.0  1.0
    # 2013-01-03 -1.235122 -1.738727  1.224550  5.0  2.0  5.0
    # 2013-01-04 -0.455281 -0.751144  0.404837  5.0  3.0  5.0
    data = pd.isna(df1)
    print(data)
    #                 A      B      C      D      F      E
    # 2013-01-01  False  False  False  False   True  False
    # 2013-01-02  False  False  False  False  False  False
    # 2013-01-03  False  False  False  False  False   True
    # 2013-01-04  False  False  False  False  False   True

missing_data()

#Operations

def stats():
    print(df.mean())
    # A   -0.544068
    # B   -0.549428
    # C    0.246495
    # D    5.000000
    # F    3.000000
    # dtype: float64
    print(df.mean(axis=1))
    # 2013-01-01    1.389103
    # 2013-01-02    1.639772
    # 2013-01-03    1.912875
    # 2013-01-04    1.535297
    # 2013-01-05    2.154783
    # 2013-01-06    1.310906
    # Freq: D, dtype: float64
    s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
    print("AAAAAAA")
    print(s)
    # 2013-01-01    NaN
    # 2013-01-02    NaN
    # 2013-01-03    1.0
    # 2013-01-04    3.0
    # 2013-01-05    5.0
    # 2013-01-06    NaN
    # Freq: D, dtype: float64
    data = df.sub(s, axis="index")
    print(data)
    #                    A         B         C    D    F
    # 2013-01-01       NaN       NaN       NaN  NaN  NaN
    # 2013-01-02       NaN       NaN       NaN  NaN  NaN
    # 2013-01-03 -1.897605 -0.890806 -0.295739  4.0  1.0
    # 2013-01-04 -3.419937 -3.702601 -2.518076  2.0  0.0
    # 2013-01-05 -5.187529 -4.233214 -6.078544  0.0 -1.0
    # 2013-01-06       NaN       NaN       NaN  NaN  NaN

stats()

def user_defined_functions():
    data = df.agg(lambda x: np.mean(x) * 5.6)
    print(data)
    # A    -0.938416
    # B    -0.852594
    # C    -2.932590
    # D    28.000000
    # F    16.800000
    # dtype: float64

user_defined_functions()

def value_counts():
    s = pd.Series(np.random.randint(0, 7, size=10))
    print(s)
    # 0    6
    # 1    6
    # 2    2
    # 3    5
    # 4    4
    # 5    0
    # 6    1
    # 7    2
    # 8    6
    # 9    4
    # dtype: int32
    print(s.value_counts())
    # 6    3
    # 2    2
    # 4    2
    # 5    1
    # 0    1
    # 1    1
    # Name: count, dtype: int64

value_counts()

def string_methods():
    s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
    print(s)
    # 0       A
    # 1       B
    # 2       C
    # 3    Aaba
    # 4    Baca
    # 5     NaN
    # 6    CABA
    # 7     dog
    # 8     cat
    # dtype: object
    print(s.str.lower())
    # 0       a
    # 1       b
    # 2       c
    # 3    aaba
    # 4    baca
    # 5     NaN
    # 6    caba
    # 7     dog
    # 8     cat
    # dtype: object


string_methods()

# Merge

def concat():
    df = pd.DataFrame(np.random.randn(10, 4))
    print(df)
    #           0         1         2         3
    # 0  0.005917 -0.263295  0.096591  1.454742
    # 1 -0.238558  1.870882 -1.992218  0.801065
    # 2  0.963679  0.244488  1.026168 -0.115969
    # 3 -0.362967 -0.448278  0.798847 -0.720086
    # 4 -0.296515 -0.437192  1.097725  1.143445
    # 5  1.501105 -1.244440  0.168660 -0.987200
    # 6 -0.949977  0.116873  0.353460 -0.222352
    # 7  0.851636  0.470350  1.218640 -1.244526
    # 8 -0.930500  1.512216 -1.372226 -1.926104
    # 9 -0.758191 -1.358127  0.049993 -0.974680
    pieces = [df[:3], df[3:7], df[7:]]
    for ind in pieces:
        print(ind)
    #           0         1         2         3
    # 0 -2.404940 -1.086954 -0.451426  0.121303
    # 1 -0.267309  1.023573  0.569767  0.677377
    # 2 -1.455317  0.091623 -1.420070  0.360868
    #           0         1         2         3
    # 3 -1.460279  0.038412  1.176861  0.086300
    # 4  0.749812 -0.061028 -0.987563  1.188260
    # 5 -1.567858  1.097559 -0.983857 -2.728454
    # 6  1.207139  0.429123  0.380038 -0.167247
    #           0         1         2         3
    # 7 -0.846151 -0.165225 -1.912624 -0.214077
    # 8 -0.329563 -1.727297  0.463362 -0.411590
    # 9 -0.933766  0.039019 -0.901803 -1.569063
    data = pd.concat(pieces)
    print(data)
    #           0         1         2         3
    # 0  1.545480  2.837031  0.949095  0.813021
    # 1  0.558722  0.660511  1.533020 -1.458659
    # 2  1.418520 -0.882485 -0.656131  1.488212
    # 3  0.939072 -1.177605  0.269829  1.263321
    # 4 -0.846987 -0.616898  0.806268  0.605285
    # 5 -1.183909 -2.237260 -1.399566  1.850161
    # 6  2.048188 -0.014971 -0.873969 -1.727536
    # 7 -0.130202 -0.130437  0.287296 -0.826797
    # 8 -0.230863  0.136214  1.019479 -0.752796
    # 9 -2.159672 -0.408865 -0.528973 -0.716998

concat()

def join():
    left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
    print(left)
    #    key  lval
    # 0  foo     1
    # 1  foo     2
    right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
    print(right)
    #    key  rval
    # 0  foo     4
    # 1  foo     5
    data = pd.merge(left, right, on="key")
    print(data)
    #    key  lval  rval
    # 0  foo     1     4
    # 1  foo     1     5
    # 2  foo     2     4
    # 3  foo     2     5

def merge():
    left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
    print(left)
    #    key  lval
    # 0  foo     1
    # 1  foo     2
    right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
    print(right)
    #    key  rval
    # 0  foo     4
    # 1  foo     5
    data = pd.merge(left, right, on="key")
    print(data)
    #    key  lval  rval
    # 0  foo     1     4
    # 1  bar     2     5

def grouping():
    df = pd.DataFrame(
        {
            "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
            "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
            "C": np.random.randn(8),
            "D": np.random.randn(8),
        }
    )

    print(df)
    #      A      B         C         D
    # 0  foo    one  0.940551 -1.110153
    # 1  bar    one -0.781680  0.405563
    # 2  foo    two -1.122291 -0.921355
    # 3  bar  three  0.042884 -1.050010
    # 4  foo    two -0.205932  0.755493
    # 5  bar    two -0.020036 -1.705372
    # 6  foo    one -2.008278 -0.810113
    # 7  foo  three -1.245866 -0.449486

    data = df.groupby("A")[["C", "D"]].sum()
    print(data)
    # A
    # bar -0.748203 -2.414909
    # foo -5.633438 -0.911877
    data = df.groupby(["A", "B"]).sum()
    print(data)
    # A   B
    # bar one    1.511763  0.396823
    #     three -0.990582 -0.532532
    #     two    1.211526  1.208843
    # foo one    1.614581 -1.658537
    #     three  0.024580 -0.264610
    #     two    1.185429  1.348368


def find_duplicates():
    array = [1,2,3,4,5,6,6,7,8,9,0]
    df = pd.DataFrame(array, columns=["COLUMN"])
    print(df)
    a1 = df.groupby(['COLUMN'])['COLUMN'].count()
    print(a1)
    print("AAAAAAA")
    print(a1.describe)
    print("BBBBBB")
    print(a1.dtypes)
    # print(a1.COLUMN)
    # a2 = a1[a1["COLUMN"]>1]
    # print(a2)
    for ind in list(a1):
        if ind>1:
            print("Duplication", ind)

    def find_duplicates_groupby():
        array = [1,2,3,4,5,6,6,7,8,9,0]
        df = pd.DataFrame(array, columns=["COLUMN"])
        a = pd.concat(g for _, g in df.groupby("COLUMN") if len(g) > 1)
        print(a)

    find_duplicates_groupby()
    #    COLUMN
    # 5       6
    # 6       6

    def find_duplicated():
        array = [1,2,3,4,5,6,6,7,8,9,0]
        df = pd.DataFrame(array, columns=["COLUMN"])
        a = df[df.duplicated(['COLUMN'], keep=False)]
        print(a)

    find_duplicated()
    #    COLUMN
    # 5       6
    # 6       6

    def find_duplicated_2():
        array = [1,2,3,4,5,6,6,7,8,9,0]
        df = pd.DataFrame(array, columns=["COLUMN"])
        dupes = df[df.duplicated()] #add keep=False and both dupes will show up
        print(dupes)

    find_duplicated_2()
    #    COLUMN
    # 6       6

find_duplicates()

def stacking():

    arrays = [
       ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
       ["one", "two", "one", "two", "one", "two", "one", "two"],
    ]
    print(arrays)
    # [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'], ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
    index = pd.MultiIndex.from_arrays(arrays, names=["first", "second"])
    print(index)
    # MultiIndex([('bar', 'one'),
    #             ('bar', 'two'),
    #             ('baz', 'one'),
    #             ('baz', 'two'),
    #             ('foo', 'one'),
    #             ('foo', 'two'),
    #             ('qux', 'one'),
    #             ('qux', 'two')],
    #            names=['first', 'second'])
    df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=["A", "B"])
    print(df)
    #                      A         B
    # first second
    # bar   one     1.128597 -1.141856
    #       two     0.822625  1.287810
    # baz   one    -1.843425 -1.545403
    #       two    -1.045454  1.183161
    # foo   one    -1.898366 -0.611088
    #       two     0.642811  0.228377
    # qux   one     0.813206 -1.226162
    #       two     0.486180 -0.822170
    df2 = df[:4]
    print(df2)
    #                      A         B
    # first second
    # bar   one     1.128597 -1.141856
    #       two     0.822625  1.287810
    # baz   one    -1.843425 -1.545403
    #       two    -1.045454  1.183161
    stacked = df2.stack(future_stack=True)
    print(stacked)
    # first  second
    # bar    one     A   -1.741912
    #                B   -1.563027
    #        two     A   -0.411315
    #                B    0.087041
    # baz    one     A   -0.218053
    #                B    0.310999
    #        two     A   -1.174621
    #                B   -1.582389
    # dtype: float64

    print(stacked.unstack())
    #                      A         B
    # first second
    # bar   one    -0.531335  0.313809
    #       two    -1.059828 -0.830210
    # baz   one     0.237802 -1.225225
    #       two    -1.327806  0.091934

    print(stacked.unstack(1))
    # second        one       two
    # first
    # bar   A -0.531335 -1.059828
    #       B  0.313809 -0.830210
    # baz   A  0.237802 -1.327806
    #       B -1.225225  0.091934

    print(stacked.unstack(0))
    # first          bar       baz
    # second
    # one    A -0.531335  0.237802
    #        B  0.313809 -1.225225
    # two    A -1.059828 -1.327806
    #        B -0.830210  0.091934

stacking()

#PIVOT TABLES
def pivot_tables():
    df = pd.DataFrame(
        {
            "A": ["one", "one", "two", "three"] * 3,
            "B": ["A", "B", "C"] * 4,
            "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
            "D": np.random.randn(12),
            "E": np.random.randn(12),
        }
    )

    print(df)
#         A  B    C         D         E
# 0     one  A  foo -1.510960  0.102360
# 1     one  B  foo  0.163227  1.207815
# 2     two  C  foo -1.759005 -1.793433
# 3   three  A  bar  1.461493  1.073468
# 4     one  B  bar -1.432255 -0.328611
# 5     one  C  bar -1.096507 -0.040675
# 6     two  A  foo  0.399496  0.472324
# 7   three  B  foo  0.278166  1.024661
# 8     one  C  foo  1.000020 -0.158077
# 9     one  A  bar -1.540859 -0.443266
# 10    two  B  bar  1.839733 -0.081167
# 11  three  C  bar  0.713523 -1.485210
    a = pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
    print(a)
# C             bar       foo
# A     B
# one   A -1.540859 -1.510960
#       B -1.432255  0.163227
#       C -1.096507  1.000020
# three A  1.461493       NaN
#       B       NaN  0.278166
#       C  0.713523       NaN
# two   A       NaN  0.399496
#       B  1.839733       NaN
#       C       NaN -1.759005

pivot_tables()

#Time Series
def time_series():
    rng = pd.date_range("1/1/2012", periods=100, freq="s")
    print(rng)
    """
    # DatetimeIndex(['2012-01-01 00:00:00', '2012-01-01 00:00:01',
    #            '2012-01-01 00:00:02', '2012-01-01 00:00:03',
    #            '2012-01-01 00:00:04', '2012-01-01 00:00:05',
    #            '2012-01-01 00:00:06', '2012-01-01 00:00:07',
    #            '2012-01-01 00:00:08', '2012-01-01 00:00:09',
    #            '2012-01-01 00:00:10', '2012-01-01 00:00:11',
    #            '2012-01-01 00:00:12', '2012-01-01 00:00:13',
    #            '2012-01-01 00:00:14', '2012-01-01 00:00:15',
    #            '2012-01-01 00:00:16', '2012-01-01 00:00:17',
    #            '2012-01-01 00:00:18', '2012-01-01 00:00:19',
    #            '2012-01-01 00:00:20', '2012-01-01 00:00:21',
    #            '2012-01-01 00:00:22', '2012-01-01 00:00:23',
    #            '2012-01-01 00:00:24', '2012-01-01 00:00:25',
    #            '2012-01-01 00:00:26', '2012-01-01 00:00:27',
    #            '2012-01-01 00:00:28', '2012-01-01 00:00:29',
    #            '2012-01-01 00:00:30', '2012-01-01 00:00:31',
    #            '2012-01-01 00:00:32', '2012-01-01 00:00:33',
    #            '2012-01-01 00:00:34', '2012-01-01 00:00:35',
    #            '2012-01-01 00:00:36', '2012-01-01 00:00:37',
    #            '2012-01-01 00:00:38', '2012-01-01 00:00:39',
    #            '2012-01-01 00:00:40', '2012-01-01 00:00:41',
    #            '2012-01-01 00:00:42', '2012-01-01 00:00:43',
    #            '2012-01-01 00:00:44', '2012-01-01 00:00:45',
    #            '2012-01-01 00:00:46', '2012-01-01 00:00:47',
    #            '2012-01-01 00:00:48', '2012-01-01 00:00:49',
    #            '2012-01-01 00:00:50', '2012-01-01 00:00:51',
    #            '2012-01-01 00:00:52', '2012-01-01 00:00:53',
    #            '2012-01-01 00:00:54', '2012-01-01 00:00:55',
    #            '2012-01-01 00:00:56', '2012-01-01 00:00:57',
    #            '2012-01-01 00:00:58', '2012-01-01 00:00:59',
    #            '2012-01-01 00:01:00', '2012-01-01 00:01:01',
    #            '2012-01-01 00:01:02', '2012-01-01 00:01:03',
    #            '2012-01-01 00:01:04', '2012-01-01 00:01:05',
    #            '2012-01-01 00:01:06', '2012-01-01 00:01:07',
    #            '2012-01-01 00:01:08', '2012-01-01 00:01:09',
    #            '2012-01-01 00:01:10', '2012-01-01 00:01:11',
    #            '2012-01-01 00:01:12', '2012-01-01 00:01:13',
    #            '2012-01-01 00:01:14', '2012-01-01 00:01:15',
    #            '2012-01-01 00:01:16', '2012-01-01 00:01:17',
    #            '2012-01-01 00:01:18', '2012-01-01 00:01:19',
    #            '2012-01-01 00:01:20', '2012-01-01 00:01:21',
    #            '2012-01-01 00:01:22', '2012-01-01 00:01:23',
    #            '2012-01-01 00:01:24', '2012-01-01 00:01:25',
    #            '2012-01-01 00:01:26', '2012-01-01 00:01:27',
    #            '2012-01-01 00:01:28', '2012-01-01 00:01:29',
    #            '2012-01-01 00:01:30', '2012-01-01 00:01:31',
    #            '2012-01-01 00:01:32', '2012-01-01 00:01:33',
    #            '2012-01-01 00:01:34', '2012-01-01 00:01:35',
    #            '2012-01-01 00:01:36', '2012-01-01 00:01:37',
    #            '2012-01-01 00:01:38', '2012-01-01 00:01:39'],
    #           dtype='datetime64[ns]', freq='s')
    """
    ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
    print(ts)
    """
# 2012-01-01 00:00:00    494
# 2012-01-01 00:00:01      6
# 2012-01-01 00:00:02     45
# 2012-01-01 00:00:03    101
# 2012-01-01 00:00:04    180
#                       ... 
# 2012-01-01 00:01:35     79
# 2012-01-01 00:01:36    227
# 2012-01-01 00:01:37    234
# 2012-01-01 00:01:38    459
# 2012-01-01 00:01:39    282
# Freq: s, Length: 100, dtype: int32
    """
    print(ts.resample("5Min").sum())
    """
    # 2012-01-01    23625
    # Freq: 5min, dtype: int32
    """

    rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
    print(rng)
    """
DatetimeIndex(['2012-03-06', '2012-03-07', '2012-03-08', '2012-03-09',
               '2012-03-10'],
              dtype='datetime64[ns]', freq='D')    
    """
    ts = pd.Series(np.random.randn(len(rng)), rng)
    print(ts)
    """
2012-03-06    0.865291
2012-03-07    0.407416
2012-03-08    0.206638
2012-03-09   -0.644254
2012-03-10    0.794952
Freq: D, dtype: float64    
    """
    ts_utc = ts.tz_localize("UTC")
    print(ts_utc)
    """
2012-03-06 00:00:00+00:00    0.865291
2012-03-07 00:00:00+00:00    0.407416
2012-03-08 00:00:00+00:00    0.206638
2012-03-09 00:00:00+00:00   -0.644254
2012-03-10 00:00:00+00:00    0.794952
Freq: D, dtype: float64
    """
    a = ts_utc.tz_convert("US/Eastern")
    print(a)
    """
# 2012-03-05 19:00:00-05:00   -0.101839
# 2012-03-06 19:00:00-05:00    3.075011
# 2012-03-07 19:00:00-05:00   -0.492729
# 2012-03-08 19:00:00-05:00    1.681448
# 2012-03-09 19:00:00-05:00   -0.354805
# Freq: D, dtype: float64    
    """
    print(rng)
    """
# Freq: D, dtype: float64
# DatetimeIndex(['2012-03-06', '2012-03-07', '2012-03-08', '2012-03-09',
#                '2012-03-10'],
#               dtype='datetime64[ns]', freq='D')
    """
    a = rng + pd.offsets.BusinessDay(5)
    print(a)
    """
# DatetimeIndex(['2012-03-13', '2012-03-14', '2012-03-15', '2012-03-16',
#                '2012-03-16'],
#               dtype='datetime64[ns]', freq=None)
    """

time_series()

#Catergorical
def categorical():
    df = pd.DataFrame(
        {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
    )
    df["grade"] = df["raw_grade"].astype("category")
    print(df["grade"])
    """
# 0    a
# 1    b
# 2    b
# 3    a
# 4    a
# 5    e
# Name: grade, dtype: category
# Categories (3, object): ['a', 'b', 'e']
    """
    new_categories = ["very good", "good", "very bad"]
    df["grade"] = df["grade"].cat.rename_categories(new_categories)
    print(df["grade"])
    """
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5     very bad
# Name: grade, dtype: category
# Categories (3, object): ['very good', 'good', 'very bad']
    """
    df["grade"] = df["grade"].cat.set_categories(
        ["very bad", "bad", "medium", "good", "very good"]
    )
    print(df["grade"])
    """
# 0    very good
# 1         good
# 2         good
# 3    very good
# 4    very good
# 5     very bad
# Name: grade, dtype: category
# Categories (5, object): ['very bad', 'bad', 'medium', 'good', 'very good']
    """
    df = df.sort_values(by="grade")
    print(df)
    """
#        id raw_grade      grade
# 5   6         e   very bad
# 1   2         b       good
# 2   3         b       good
# 0   1         a  very good
# 3   4         a  very good
# 4   5         a  very good
    """
    df = df.groupby("grade", observed=False).size()
    print(df)
    """
# grade
# very bad     1
# bad          0
# medium       0
# good         2
# very good    3
# dtype: int64
    """

categorical()

# Plotting
def plotting():
    print("111111111111")
    plt.close("all")
    ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
    ts = ts.cumsum()
    print("2222222222222")
    ts.plot()
    print("3333333333333")
    df = pd.DataFrame(
        np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
    )
    df = df.cumsum()
    plt.figure()
    print("44444444444")
    df.plot()
    plt.legend(loc='best')
    print("555555555555")
plotting()

#Import Export
def import_export():
    df = pd.DataFrame(np.random.randint(0, 5, (10, 5)))
    print(df)
    """
    #     0  1  2  3  4
    # 0  1  2  3  3  4
    # 1  3  2  2  0  1
    # 2  1  2  4  0  2
    # 3  0  1  4  3  4
    # 4  2  3  0  4  2
    # 5  2  1  3  2  2
    # 6  4  1  4  2  4
    # 7  2  4  1  1  1
    # 8  0  1  4  2  0
    # 9  2  0  1  1  4
    """
    df.to_csv("foo.csv")
    a = pd.read_csv("../code2/foo.csv")
    print(a)
    """
#        Unnamed: 0  0  1  2  3  4
# 0           0  1  2  3  3  4
# 1           1  3  2  2  0  1
# 2           2  1  2  4  0  2
# 3           3  0  1  4  3  4
# 4           4  2  3  0  4  2
# 5           5  2  1  3  2  2
# 6           6  4  1  4  2  4
# 7           7  2  4  1  1  1
# 8           8  0  1  4  2  0
# 9           9  2  0  1  1  4
    """
    df.to_parquet("foo.parquet")
    a = pd.read_parquet("../code2/foo.parquet")
    print(a)
    """
#     0  1  2  3  4
# 0  1  3  0  3  2
# 1  4  2  1  0  0
# 2  1  2  3  2  0
# 3  0  4  4  0  4
# 4  4  1  0  0  2
# 5  1  3  0  3  4
# 6  3  4  1  4  1
# 7  1  4  1  2  3
# 8  2  1  1  2  4
# 9  4  4  2  2  2
    """
    df.to_excel("foo.xlsx", sheet_name="Sheet1")
    a = pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"])
    print(a)
    """
#        Unnamed: 0  0  1  2  3  4
# 0           0  4  2  1  0  0
# 1           1  2  0  1  1  1
# 2           2  4  2  1  4  3
# 3           3  4  2  0  3  0
# 4           4  2  3  3  3  0
# 5           5  4  3  4  2  2
# 6           6  3  2  0  0  1
# 7           7  4  0  1  2  1
# 8           8  1  2  3  3  0
# 9           9  0  1  4  3  0
    """
import_export()

#Gotchas
def gotchas():
    a = pd.Series([False, True, False])
    print("data =\n", a)
    print("a.empty =", a.empty)
    print("a[1].item() =", a[1].item())
    print("a.all() =", a.all())
    # if pd.Series(a):
    #      print("I was true")
gotchas()
