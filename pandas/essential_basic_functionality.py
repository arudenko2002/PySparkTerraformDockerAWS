import numpy as np
import pandas as pd

def essential_basic_functionality():
    index = pd.date_range("1/1/2000", periods=8)
    print(index)
    """
    DatetimeIndex(['2000-01-01', '2000-01-02', '2000-01-03', '2000-01-04',
               '2000-01-05', '2000-01-06', '2000-01-07', '2000-01-08'],
              dtype='datetime64[ns]', freq='D')
    """
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s)
    """
    a   -0.661155
    b    1.446389
    c    0.088210
    d   -0.328302
    e    0.831805
    dtype: float64
    """
    df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=["A", "B", "C"])
    print(df)
    """
                       A         B         C
    2000-01-01 -1.535016 -0.904877 -1.077748
    2000-01-02  0.307564 -0.236752 -1.610167
    2000-01-03 -0.279150 -0.444291  0.738935
    2000-01-04 -0.428961  0.192570 -0.004866
    2000-01-05 -2.548732 -1.503260 -0.783418
    2000-01-06 -0.847026  0.590929  0.769079
    2000-01-07 -1.520426  1.044636  0.176145
    2000-01-08 -0.456944  0.315307  0.946533
    """

    long_series = pd.Series(np.random.randn(1000))
    print(long_series.head())
    """
    0    0.627707
    1    1.793164
    2    0.208167
    3   -0.890842
    4   -0.506921
    dtype: float64
    """
    print(long_series.tail(3))
    """
    997    0.492503
    998   -0.273277
    999   -0.613031
    dtype: float64
    """
    print(df[:2])
    """
                       A         B         C
    2000-01-01  0.284218 -0.393822 -0.195337
    2000-01-02 -0.918015  0.046770  1.328676
    """
    df.columns = [x.lower() for x in df.columns]
    print(s.array)
    """
    <NumpyExtensionArray>
    [  np.float64(0.5712218820222915), np.float64(-0.30123500098279377),
     np.float64(-0.09370514992751336),   np.float64(0.5268302575193428),
     np.float64(-0.37976282831748576)]
    Length: 5, dtype: float64
    """
    print(s.index.array)
    """
    ['a', 'b', 'c', 'd', 'e']
    Length: 5, dtype: object
    """
    print(s.to_numpy())
    """
    [-0.47143504 -0.30514553 -0.42591955  0.07693382  2.45567646]
    """
    print(np.asarray(s))
    """
    [-0.47143504 -0.30514553 -0.42591955  0.07693382  2.45567646]
    """
    ser = pd.Series(pd.date_range("2000", periods=2, tz="CET"))
    print(ser)
    """
    0   2000-01-01 00:00:00+01:00
    1   2000-01-02 00:00:00+01:00
    dtype: datetime64[ns, CET]
    """
    print(ser.to_numpy(dtype=object))
    """
    [Timestamp('2000-01-01 00:00:00+0100', tz='CET')
    Timestamp('2000-01-02 00:00:00+0100', tz='CET')]
    """
    print(ser.to_numpy(dtype="datetime64[ns]"))
    """
    ['1999-12-31T23:00:00.000000000' '2000-01-01T23:00:00.000000000']
    """
    print(df.to_numpy())
    """
    [[ 2.28200481  0.0942968  -0.11513531]
     [-0.16253022  0.54882077 -1.09243731]
     [-1.05703368  0.6558491   0.91695089]
     [ 0.65083172 -0.63787994 -0.40305266]
     [-0.58763058 -0.67179207  0.07812538]
     [-2.46439874  2.90189428 -0.18764202]
     [-0.95575895  0.92517296 -0.33989508]
     [-0.12537274  2.37285647 -0.5334798 ]]
    """
    pd.set_option("compute.use_bottleneck", False)
    pd.set_option("compute.use_numexpr", False)

    df = pd.DataFrame(
        {
            "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
            "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
            "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
        }
    )
    print(df)
    """
            one       two     three
    a  0.377486  1.411873       NaN
    b -0.040712 -0.689912 -0.311858
    c -2.163479 -1.130724  0.995659
    d       NaN  0.319128  1.133514
    """
    row = df.iloc[1]
    print(row)
    """
    one      0.661082
    two      0.135605
    three   -0.008578
    Name: b, dtype: float64
    """
    column = df["two"]
    print(column)
    """
    a   -0.214955
    b   -0.077172
    c   -0.496959
    d    0.440552
    Name: two, dtype: float64
    """
    print(df.sub(row, axis="columns"))
    """
            one       two     three
    a -1.534506  0.659444       NaN
    b  0.000000  0.000000  0.000000
    c -2.906522  0.133112 -0.288727
    d       NaN -1.052738 -0.359201
    """
    print(df.sub(row, axis=1))
    """
            one       two     three
    a  2.155966 -1.937733       NaN
    b  0.000000  0.000000  0.000000
    c  1.555940 -0.989913  1.156412
    d       NaN  0.930324 -1.389314
    """
    print(df.sub(column, axis="index"))
    """
            one  two     three
    a  1.049016  0.0       NaN
    b  0.932117  0.0  0.416018
    c -1.473508  0.0 -1.557402
    d       NaN  0.0 -1.040062
    """
    print(df.sub(column, axis=0))
    """
            one  two     three
    a -1.826998  0.0       NaN
    b -0.995408  0.0  0.305339
    c  1.860569  0.0 -0.466978
    d       NaN  0.0  0.496687
    """
    dfmi = df.copy()
    print(dfmi)
    """
            one       two     three
    a -0.467980  0.859509       NaN
    b -0.524182 -0.656906  0.485271
    c  0.394924  0.697751 -0.661294
    d       NaN  1.230037 -0.491761
    """
    dfmi.index = pd.MultiIndex.from_tuples(
        [(1, "a"), (1, "b"), (1, "c"), (2, "a")], names=["first", "second"]
    )
    print(dfmi.index)
    """
    MultiIndex([(1, 'a'),
            (1, 'b'),
            (1, 'c'),
            (2, 'a')],
           names=['first', 'second'])
    """
    print(dfmi.sub(column, axis=0, level="second"))
    """
    first second                              
    1     a      -0.094102  0.000000       NaN
          b      -2.558797  0.000000 -3.297609
          c       1.645336  0.000000  0.990015
    2     a            NaN  0.617574  0.931517
    """

    s = pd.Series(np.arange(10))
    print(s)
    """
    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    6    6
    7    7
    8    8
    9    9
    """
    div, rem = divmod(s, 3)
    print(div)
    """
    0    0
    1    0
    2    0
    3    1
    4    1
    5    1
    6    2
    7    2
    8    2
    9    3
    dtype: int64
    """
    print(rem)
    """
    0    0
    1    1
    2    2
    3    0
    4    1
    5    2
    6    0
    7    1
    8    2
    9    0
    dtype: int64
    """
    idx = pd.Index(np.arange(10))
    print(idx)
    """
    Index([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int64')
    """
    div, rem = divmod(idx, 3)
    print(div)
    """
    Index([0, 0, 0, 1, 1, 1, 2, 2, 2, 3], dtype='int64')
    """
    print(rem)
    """
    Index([0, 1, 2, 0, 1, 2, 0, 1, 2, 0], dtype='int64')
    """

    print(s)
    """
    0    0
    1    1
    2    2
    3    3
    4    4
    5    5
    6    6
    7    7
    8    8
    9    9
    dtype: int64
    """
    div, rem = divmod(s, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6])
    print(div)
    """
    0    0
    1    0
    2    0
    3    1
    4    1
    5    1
    6    1
    7    1
    8    1
    9    1
    dtype: int64
    """
    print(rem)
    """
    0    0
    1    1
    2    2
    3    0
    4    0
    5    1
    6    1
    7    2
    8    2
    9    3
    dtype: int64
    """

    df2 = df.copy()
    df2.loc["a", "three"] = 1.0
    print(df)
    """
            one       two     three
    a -0.394856 -0.037144       NaN
    b -1.110899  1.692745  0.576693
    c -0.273794 -1.118215 -1.045689
    d       NaN  0.079231 -1.203351
    """
    print(df2)
    """
            one       two     three
    a -0.394856 -0.037144  1.000000
    b -1.110899  1.692745  0.576693
    c -0.273794 -1.118215 -1.045689
    d       NaN  0.079231 -1.203351
    """
    print(df+df2)
    """
            one       two     three
    a -0.789713 -0.074287       NaN
    b -2.221798  3.385490  1.153387
    c -0.547588 -2.236430 -2.091377
    d       NaN  0.158462 -2.406702
    """
    print(df.add(df2, fill_value=0))
    """
            one       two     three
    a -0.789713 -0.074287  1.000000
    b -2.221798  3.385490  1.153387
    c -0.547588 -2.236430 -2.091377
    d       NaN  0.158462 -2.406702
    """

    print(df.gt(df2))
    """
         one    two  three
    a  False  False  False
    b  False  False  False
    c  False  False  False
    d  False  False  False
    """
    print(df2.ne(df))
    """
         one    two  three
    a  False  False   True
    b  False  False  False
    c  False  False  False
    d   True  False  False
    """

    print((df > 0).any().any())
    """
    True
    """

    print(df.empty)
    """
    False
    """

    v = pd.DataFrame(columns=list("ABC")).empty
    print(v)
    """
    True
    """

    print(df + df == df * 2)
    """
         one   two  three
    a   True  True  False
    b   True  True   True
    c   True  True   True
    d  False  True   True
    """
    print((df + df == df * 2).all())
    """
    one      False
    two       True
    three    False
    dtype: bool
    """

    print(np.nan == np.nan)
    """
    False
    """

    print((df + df).equals(df * 2))
    """
    True
    """

    df1 = pd.DataFrame({"col": ["foo", 0, np.nan]})
    print(df1)
    df2 = pd.DataFrame({"col": [np.nan, 0, "foo"]}, index=[2, 1, 0])
    print(df2)

    print(df1.equals(df2))
    """
    False
    """

    print(df1.equals(df2.sort_index()))
    """
    True
    """

    data = pd.Series(["foo", "bar", "baz"]) == "foo"
    print(data)
    """
    0     True
    1    False
    2    False
    """
    print(pd.Index(["foo", "bar", "baz"]) == "foo")
    """
    [ True False False]
    """

    data = pd.Series(["foo", "bar", "baz"]) == pd.Index(["foo", "bar", "qux"])
    print(data)
    """
    0     True
    1     True
    2    False
    dtype: bool
    """
    data = pd.Series(["foo", "bar", "baz"]) == np.array(["foo", "bar", "qux"])
    print(data)
    """
    0     True
    1     True
    2    False
    dtype: bool
    """

    df1 = pd.DataFrame(
        {"A": [1.0, np.nan, 3.0, 5.0, np.nan], "B": [np.nan, 2.0, 3.0, np.nan, 6.0]}
    )

    print(df1)
    """
         A    B
    0  1.0  NaN
    1  NaN  2.0
    2  3.0  3.0
    3  5.0  NaN
    4  NaN  6.0
    """

    df2 = pd.DataFrame(
        {
            "A": [5.0, 2.0, 4.0, np.nan, 3.0, 7.0],
            "B": [np.nan, np.nan, 3.0, 4.0, 6.0, 8.0],
        }
    )

    print(df2)
    """
         A    B
    0  5.0  NaN
    1  2.0  NaN
    2  4.0  3.0
    3  NaN  4.0
    4  3.0  6.0
    5  7.0  8.0
    """
    print(df1.combine_first(df2))
    """
         A    B
    0  1.0  NaN
    1  2.0  2.0
    2  3.0  3.0
    3  5.0  4.0
    4  3.0  6.0
    5  7.0  8.0
    """

    # General DataFrame combine
    def combiner(x, y):
        return np.where(pd.isna(x), y, x)

    data = df1.combine(df2, combiner)
    print(data)
    """
         A    B
    0  1.0  NaN
    1  2.0  2.0
    2  3.0  3.0
    3  5.0  4.0
    4  3.0  6.0
    5  7.0  8.0
    """

    # Descriptive statistics
    print(df)
    """
            one       two     three
    a -0.991330 -0.216918       NaN
    b  0.980546 -0.249442  0.381066
    c -1.718887  0.933565  0.456019
    d       NaN  1.712912 -1.166048
    """
    print("AAAAAAA")
    print(df.mean(0))
    """
    one     -0.576557
    two      0.545029
    three   -0.109654
    dtype: float64
    """
    print(df.mean(1))
    """
    a   -0.045731
    b    0.477065
    c    0.514890
    d   -0.170425
    dtype: float64
    """
    print(df.sum(0, skipna=False))
    """
    one           NaN
    two      2.646662
    three         NaN
    dtype: float64
    """
    print(df.sum(axis=1, skipna=True))
    """
    a   -0.091462
    b    1.431194
    c    1.544671
    d   -0.340850
    dtype: float64
    """

    ts_stand = (df - df.mean()) / df.std()
    print(ts_stand.std())
    """
    one      1.0
    two      1.0
    three    1.0
    dtype: float64
    """
    xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
    print(xs_stand.std(1))
    """
    a    1.0
    b    1.0
    c    1.0
    d    1.0
    dtype: float64
    """
    print(df.cumsum())
    """
            one       two     three
    a -0.899752 -1.153878       NaN
    b -2.427538 -2.510879 -0.062174
    c -2.543874 -1.910369 -1.277260
    d       NaN  0.462535 -1.830436
    """

    """
    Function  Description
    count     Number of non-NA observations
    sum       Sum of values
    mean      Mean of values
    median    Arithmetic median of values
    min       Minimum
    max       Maximum
    mode      Mode
    abs       Absolute Value
    prod      Product of values
    std       Bessel-corrected sample standard deviation
    var       Unbiased variance
    sem       Standard error of the mean
    skew      Sample skewness (3rd moment)
    kurt      Sample kurtosis (4th moment)
    quantile  Sample quantile (value at %)
    cumsum    Cumulative sum
    cumprod   Cumulative product
    cummax    Cumulative maximum
    cummin    Cumulative minimum
    """

    # Note that by chance some NumPy methods, like mean, std, and sum, will exclude NAs on Series input by default:
    print(np.mean(df["one"]))
    """
    0.06981401335986274
    """
    print(np.mean(df["one"].to_numpy()))
    """
    nan
    """

    series = pd.Series(np.random.randn(500))
    series[20:500] = np.nan
    series[10:20] = 5
    print(series.nunique())
    """
    11
    """

    # Describe
    series = pd.Series(np.random.randn(1000))
    series[::2] = np.nan
    print(series.describe())
    """
    count    500.000000
    mean      -0.024778
    std        0.982289
    min       -2.912189
    25%       -0.654417
    50%       -0.027243
    75%        0.603704
    max        2.996212
    dtype: float64
    """
    frame = pd.DataFrame(np.random.randn(1000, 5), columns=["a", "b", "c", "d", "e"])
    frame.iloc[::2] = np.nan
    print(frame.describe())
    """
                    a           b           c           d           e
    count  500.000000  500.000000  500.000000  500.000000  500.000000
    mean     0.033387    0.030045   -0.043719   -0.051686    0.005979
    std      1.017152    0.978743    1.025270    1.015988    1.006695
    min     -3.000951   -2.637901   -3.303099   -3.159200   -3.188821
    25%     -0.647623   -0.576449   -0.712369   -0.691338   -0.691115
    50%      0.047578   -0.021499   -0.023888   -0.032652   -0.025363
    75%      0.729907    0.775880    0.618896    0.670047    0.649748
    max      2.740139    2.752332    3.004229    2.728702    3.240991
    """
    print(series.describe(percentiles=[0.05, 0.25, 0.75, 0.95]))
    """
    count    500.000000
    mean       0.004551
    std        0.953456
    min       -3.084357
    5%        -1.600808
    25%       -0.644781
    50%        0.037244
    75%        0.673155
    95%        1.624739
    max        2.761881
    dtype: float64
    """

    s = pd.Series(["a", "a", "b", "b", "a", "a", np.nan, "c", "d", "a"])
    print(s.describe())
    """
    count     9
    unique    4
    top       a
    freq      5
    dtype: object
    """

    frame = pd.DataFrame({"a": ["Yes", "Yes", "No", "No"], "b": range(4)})
    print(frame.describe())
    """
                  b
    count  4.000000
    mean   1.500000
    std    1.290994
    min    0.000000
    25%    0.750000
    50%    1.500000
    75%    2.250000
    max    3.000000
    """
    print("AAAAAAA")
    print(frame.describe(include=["object"]))
    """
              a
    count     4
    unique    2
    top     Yes
    freq      2
    """
    print(frame.describe(include=["number"]))
    """
                  b
    count  4.000000
    mean   1.500000
    std    1.290994
    min    0.000000
    25%    0.750000
    50%    1.500000
    75%    2.250000
    max    3.000000
    """
    print(frame.describe(include="all"))
    """
              a         b
    count     4  4.000000
    unique    2       NaN
    top     Yes       NaN
    freq      2       NaN
    mean    NaN  1.500000
    std     NaN  1.290994
    min     NaN  0.000000
    25%     NaN  0.750000
    50%     NaN  1.500000
    75%     NaN  2.250000
    max     NaN  3.000000
    """

    # Index of min/max values
    s1 = pd.Series([0.264410, 0.528004, 0.322093, 1.613851, -0.345763])
    print(s1)
    """
    0    0.264410
    1    0.528004
    2    0.322093
    3    1.613851
    4   -0.345763
    dtype: float64
    """
    print(s1.idxmin(), s1.idxmax())
    """
    4 3
    """
    df1 = pd.DataFrame(np.random.randn(5, 3), columns=["A", "B", "C"])
    print(df1)
    """
          A         B         C
    0 -1.452069 -1.286223 -1.082894
    1 -1.955429 -0.865559  1.179118
    2  1.417491  0.445941 -0.590242
    3  1.595449  0.170995 -0.566949
    4 -0.583322 -1.146839 -1.650604
    """
    print(df1.idxmin(axis=0))
    """
    A    1
    B    0
    C    4
    dtype: int64
    """
    print(df1.idxmax(axis=1))
    """
    0    C
    1    C
    2    A
    3    A
    4    A
    dtype: object
    """
    df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=["A"], index=list("edcba"))
    print(df3)
    """
         A
    e  2.0
    d  1.0
    c  1.0
    b  3.0
    a  NaN
    """
    print(df3["A"].idxmin())
    """
    d
    """
    data = np.random.randint(0, 7, size=50)
    print(data)
    """
    [6 3 6 6 6 2 6 5 4 3 0 1 5 3 6 2 3 4 3 1 1 0 3 5 3 5 1 6 5 1 2 1 1 0 5 0 0 3 1 0 3 2 2 5 4 2 3 6 2 0]
    """
    s = pd.Series(data)
    print(s.value_counts())
    """
    3    10
    6     8
    1     8
    2     7
    5     7
    0     7
    4     3
    Name: count, dtype: int64
    """
    data = {"a": [1, 2, 3, 4], "b": ["x", "x", "y", "y"]}
    frame = pd.DataFrame(data)
    print(frame)
    """
       a  b
    0  1  x
    1  2  x
    2  3  y
    3  4  y
    """
    print(frame.value_counts())
    """
    a  b
    1  x    1
    2  x    1
    3  y    1
    4  y    1
    """

    s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
    print(s5)
    """
    0    1
    1    1
    2    3
    3    3
    4    3
    5    5
    6    5
    7    7
    8    7
    9    7
    dtype: int64
    """
    print(s5.mode())
    """
    0    3
    1    7
    dtype: int64
    """
    df5 = pd.DataFrame(
        {
            "A": np.random.randint(0, 7, size=50),
            "B": np.random.randint(-10, 15, size=50),
        }
    )
    print(df5)
    """
        A   B
    0   0  13
    1   2   8
    2   3 -10
    3   6   6
    4   4  -5
    5   4   8
    6   0   0
    7   5  -8
    8   6   2
    9   6   3
    10  4  10
    11  6  11
    12  3  -2
    13  5  -6
    14  4  -7
    15  4  14
    16  2  11
    17  0  10
    18  5   2
    19  1   3
    20  0   4
    21  6  13
    22  3  -7
    23  1   0
    24  3  -4
    25  5   2
    26  6 -10
    27  4   6
    28  5   1
    29  0  13
    30  0   8
    31  5  -5
    32  3   8
    33  2  11
    34  5  -1
    35  4  -5
    36  0   5
    37  6  14
    38  5  -1
    39  4  -8
    40  5  -2
    41  2   3
    42  1   6
    43  3  -8
    44  3  -8
    45  1   7
    46  4  11
    47  3   9
    48  3   5
    49  3   0
    """
    print(df5.mode())
    """
         A   B
    0  3.0  -8
    1  NaN   8
    2  NaN  11
    """
    # CUT
    arr = np.random.randn(20)
    print(arr)
    """
    [-0.27644108 -1.35114631  0.1386081   0.64337416  0.17225548 -0.56966901
     -0.8237195   0.86206219  0.4984685   0.39681342 -0.01317125 -0.70545493
      1.59213015  0.12583991 -0.72863853  1.032827   -1.12293062 -0.69712925
     -1.13074888  0.38247569]
    """
    factor = pd.cut(arr, 4)
    print(factor)
    """
    [(-0.615, 0.12], (-1.354, -0.615], (0.12, 0.856], (0.12, 0.856], (0.12, 0.856], ..., (0.856, 1.592], (-1.354, -0.615], (-1.354, -0.615], (-1.354, -0.615], (0.12, 0.856]]
    Length: 20
    Categories (4, interval[float64, right]): [(-1.354, -0.615] < (-0.615, 0.12] < (0.12, 0.856] <
                                               (0.856, 1.592]]
    """
    factor = pd.cut(arr, [-5, -1, 0, 1, 5])
    print(factor)
    """
    [(-1, 0], (-5, -1], (0, 1], (0, 1], (0, 1], ..., (1, 5], (-5, -1], (-1, 0], (-5, -1], (0, 1]]
    Length: 20
    Categories (4, interval[int64, right]): [(-5, -1] < (-1, 0] < (0, 1] < (1, 5]]
    """
    # QCUT
    arr = np.random.randn(30)
    print(arr)
    """
    [-1.2168435   0.27637141  1.46045789  0.86431256 -0.77657024  0.15635757
      1.55518864 -0.62115025  1.11557009 -0.18285758 -0.18026662  1.16276422
     -1.00069993  0.03999047  2.81191161  0.26592597  1.50032379 -1.4266324
     -0.2143984   1.28027492  0.69092781 -0.01808352 -0.36226983  1.45451493
     -0.89550766  0.46280846 -0.30567128  1.51113344  0.04050756 -0.55388644]
    """
    factor = pd.qcut(arr, [0, 0.25, 0.5, 0.75, 1])
    print(factor)
    """
    [(-1.428, -0.348], (0.0984, 1.151], (1.151, 2.812], (0.0984, 1.151], (-1.428, -0.348], ..., (0.0984, 1.151], (-0.348, 0.0984], (1.151, 2.812], (-0.348, 0.0984], (-1.428, -0.348]]
    Length: 30
    Categories (4, interval[float64, right]): [(-1.428, -0.348] < (-0.348, 0.0984] < (0.0984, 1.151] <
                                               (1.151, 2.812]]
    """
    # We can also pass infinite values to define the bins:
    arr = np.random.randn(20)
    print(arr)
    """
    [-0.19250139  0.56050111  0.3091071  -1.82024845  1.32791652  0.00931416
      1.55890717 -0.64793855  1.54546172  0.08148858  0.57208845 -0.41782
     -0.66021949  0.01013016  0.60272292 -1.41347648 -0.11326912  0.01582975
     -0.19859563 -1.14698344]
    """
    factor = pd.cut(arr, [-np.inf, 0, np.inf])
    print(factor)
    """
    [(-inf, 0.0], (0.0, inf], (0.0, inf], (-inf, 0.0], (0.0, inf], ..., (-inf, 0.0], (-inf, 0.0], (0.0, inf], (-inf, 0.0], (-inf, 0.0]]
    Length: 20
    Categories (2, interval[float64, right]): [(-inf, 0.0] < (0.0, inf]]
    """

    # FUNCTION APPLICATION
    def extract_city_name(df):
        """
        Chicago, IL -> Chicago for city_name column
        """
        df["city_name"] = df["city_and_code"].str.split(",").str.get(0)
        return df

    def add_country_name(df, country_name=None):
        """
        Chicago -> Chicago-US for city_name column
        """
        col = "city_name"
        df["city_and_country"] = df[col] + country_name
        return df

    df_p = pd.DataFrame({"city_and_code": ["Chicago, IL"]})
    print(add_country_name(extract_city_name(df_p), country_name="US"))
    """
      city_and_code city_name city_and_country
    0   Chicago, IL   Chicago        ChicagoUS
    """
    # is equivalent to
    print(df_p.pipe(extract_city_name).pipe(add_country_name, country_name="US"))
    """
      city_and_code city_name city_and_country
    0   Chicago, IL   Chicago        ChicagoUS
    """

    import statsmodels.formula.api as sm

    # bb = pd.read_csv("data/baseball.csv", index_col="id")
    #
    # (
    #     bb.query("h > 0")
    #     .assign(ln_h=lambda df: np.log(df.h))
    #     .pipe((sm.ols, "data"), "hr ~ ln_h + year + g + C(lg)")
    #     .fit()
    #     .summary()
    # )

    """
                               OLS Regression Results
    ==============================================================================
    Dep. Variable:                     hr   R-squared:                       0.685
    Model:                            OLS   Adj. R-squared:                  0.665
    Method:                 Least Squares   F-statistic:                     34.28
    Date:                Tue, 22 Nov 2022   Prob (F-statistic):           3.48e-15
    Time:                        05:34:17   Log-Likelihood:                -205.92
    No. Observations:                  68   AIC:                             421.8
    Df Residuals:                      63   BIC:                             432.9
    Df Model:                           4
    Covariance Type:            nonrobust
    ===============================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
    -------------------------------------------------------------------------------
    Intercept   -8484.7720   4664.146     -1.819      0.074   -1.78e+04     835.780
    C(lg)[T.NL]    -2.2736      1.325     -1.716      0.091      -4.922       0.375
    ln_h           -1.3542      0.875     -1.547      0.127      -3.103       0.395
    year            4.2277      2.324      1.819      0.074      -0.417       8.872
    g               0.1841      0.029      6.258      0.000       0.125       0.243
    ==============================================================================
    Omnibus:                       10.875   Durbin-Watson:                   1.999
    Prob(Omnibus):                  0.004   Jarque-Bera (JB):               17.298
    Skew:                           0.537   Prob(JB):                     0.000175
    Kurtosis:                       5.225   Cond. No.                     1.49e+07
    ==============================================================================
    """

    print(df)
    """
            one       two     three
    a -1.138843  0.374443       NaN
    b -2.088452 -1.199771 -0.633708
    c -0.312246 -0.102371 -0.237049
    d       NaN  0.536655 -0.120127
    """
    print(df.apply(lambda x: np.mean(x)))
    """
    one     -0.871390
    two     -0.206471
    three    0.844171
    dtype: float64
    """
    print(df.apply(lambda x: np.mean(x), axis=1))
    """
    a   -0.932950
    b   -0.019364
    c    0.016423
    d    0.483592
    dtype: float64
    """
    print(df.apply(lambda x: x.max() - x.min()))
    """
    one      1.381250
    two      2.627737
    three    0.810823
    dtype: float64
    """
    print(df.apply(np.cumsum))
    """
            one       two     three
    a -0.179156 -1.686743       NaN
    b -1.739562 -0.745750  0.561320
    c -2.614170 -0.420923  1.160369
    d       NaN -0.825882  2.532512
    """
    print(df.apply(np.exp))
    """
            one       two     three
    a  0.835976  0.185121       NaN
    b  0.210051  2.562526  1.752985
    c  0.417025  1.383792  1.820386
    d       NaN  0.667004  3.943792
    """
    print(df.apply("mean"))
    """
    one     -0.871390
    two     -0.206471
    three    0.844171
    dtype: float64
    """
    print(df.apply("mean", axis=1))
    """
    a   -0.932950
    b   -0.019364
    c    0.016423
    d    0.483592
    dtype: float64
    """
    print("BBBBBBB")
    tsdf = pd.DataFrame(
        np.random.randn(1000, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=1000),
    )
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.954594 -0.553720  0.894152
    2000-01-02 -1.534907  0.289761 -2.166976
    2000-01-03 -0.539968 -0.132607 -0.068872
    2000-01-04  0.403697 -0.470746  1.049179
    2000-01-05 -0.754082  0.808558 -0.194983
    ...              ...       ...       ...
    2002-09-22 -1.420665  1.645822 -0.918949
    2002-09-23 -0.201354  0.091187 -0.409497
    2002-09-24 -0.500994  1.779537  0.360066
    2002-09-25  2.020835  0.638541  0.351632
    2002-09-26  0.759854 -0.767955  0.919467
    """
    print(tsdf.apply(lambda x: x.idxmax()))
    """
    [1000 rows x 3 columns]
    A   2001-12-24
    B   2002-02-27
    C   2000-07-14
    dtype: datetime64[ns]
    """

    def subtract_and_divide(x, sub, divide=1):
        return (x - sub) / divide

    df_udf = pd.DataFrame(np.ones((2, 2)))
    print(df_udf)
    """
         0    1
    0  1.0  1.0
    1  1.0  1.0
    """
    print(df_udf.apply(subtract_and_divide, args=(5,), divide=3))
    """
              0         1
    0 -1.333333 -1.333333
    1 -1.333333 -1.333333
    """

    tsdf = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=10),
    )

    print(tsdf)
    """
                       A         B         C
    2000-01-01 -0.441811  1.070560  0.250077
    2000-01-02  0.267388 -1.480924  0.211016
    2000-01-03  0.782069 -0.839633  1.134042
    2000-01-04  0.713489 -0.716894 -0.564090
    2000-01-05  0.962860 -0.164018 -0.262415
    2000-01-06 -1.185264 -0.949923 -0.758341
    2000-01-07 -2.935441  1.790902  0.209522
    2000-01-08 -0.538704 -1.262024  0.141628
    2000-01-09  1.149852  0.313572 -2.135448
    2000-01-10  2.085279  1.185438  0.696550
    """
    tsdf.iloc[3:7] = np.nan
    print(tsdf)
    """
                           A         B         C
    2000-01-01 -0.441811  1.070560  0.250077
    2000-01-02  0.267388 -1.480924  0.211016
    2000-01-03  0.782069 -0.839633  1.134042
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08 -0.538704 -1.262024  0.141628
    2000-01-09  1.149852  0.313572 -2.135448
    2000-01-10  2.085279  1.185438  0.696550
    """
    print(tsdf.apply(pd.Series.interpolate))
    """
                       A         B         C
    2000-01-01 -0.441811  1.070560  0.250077
    2000-01-02  0.267388 -1.480924  0.211016
    2000-01-03  0.782069 -0.839633  1.134042
    2000-01-04  0.517914 -0.924111  0.935559
    2000-01-05  0.253760 -1.008590  0.737076
    2000-01-06 -0.010395 -1.093068  0.538594
    2000-01-07 -0.274549 -1.177546  0.340111
    2000-01-08 -0.538704 -1.262024  0.141628
    2000-01-09  1.149852  0.313572 -2.135448
    2000-01-10  2.085279  1.185438  0.696550
    """

    # Aggregation API

    tsdf = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=10),
    )
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.928137  0.645790  0.687910
    2000-01-02  2.577167  0.144269  0.918680
    2000-01-03 -1.467947 -0.068362  0.155211
    2000-01-04  0.548136  0.747377 -0.053304
    2000-01-05 -0.754816  0.501852  1.257619
    2000-01-06 -0.598128 -0.571635  0.674992
    2000-01-07 -1.126896  0.484851  1.884952
    2000-01-08 -1.340103  1.701881 -1.932946
    2000-01-09 -0.008198 -0.147240  0.229264
    2000-01-10  1.010604  0.305456 -0.855137
    """
    tsdf.iloc[3:7] = np.nan
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.928137  0.645790  0.687910
    2000-01-02  2.577167  0.144269  0.918680
    2000-01-03 -1.467947 -0.068362  0.155211
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08 -1.340103  1.701881 -1.932946
    2000-01-09 -0.008198 -0.147240  0.229264
    2000-01-10  1.010604  0.305456 -0.855137
    """
    print(tsdf.agg(lambda x: np.sum(x)))
    """
    A    1.699661
    B    2.581794
    C   -0.797018
    dtype: float64
    """
    print(tsdf.agg("sum"))
    """
    A    1.699661
    B    2.581794
    C   -0.797018
    dtype: float64
    """
    print(tsdf.sum())
    """
    A    1.699661
    B    2.581794
    C   -0.797018
    dtype: float64
    """
    print(tsdf["A"].agg("sum"))
    """
    1.699661042150987
    """

    #  Aggregating with multiple functions
    print(tsdf.agg(["sum"]))
    """
                A         B         C
    sum  5.271177  3.410813 -0.340563
    """
    print(tsdf.agg(["sum", "mean"]))
    """
                 A         B         C
    sum   5.271177  3.410813 -0.340563
    mean  0.878529  0.568469 -0.056760
    """
    print(tsdf["A"].agg(["sum", "mean"]))
    """
    sum     5.271177
    mean    0.878529
    """
    print(tsdf["A"].agg(["sum", lambda x: x.mean()]))
    """
    Name: A, dtype: float64
    sum         5.271177
    <lambda>    0.878529
    """

    def mymean(x):
        return x.mean()

    print(tsdf["A"].agg(["sum", mymean]))
    """
    Name: A, dtype: float64
    sum       5.271177
    mymean    0.878529
    Name: A, dtype: float64
    """

    # aggregating with a dict
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.230332 -2.476825  0.466247
    2000-01-02  0.247178  1.300293  0.853665
    2000-01-03  1.536254 -1.886341 -0.382776
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  1.839447  2.468879  1.184428
    2000-01-09 -1.146306  0.806567  0.268067
    2000-01-10 -0.217188 -0.624866  0.725445
    """
    print(tsdf.agg({"A": "mean", "B": "sum"}))
    """
    A    0.414953
    B   -0.412294
    dtype: float64
    """
    print(tsdf.agg({"A": ["mean", "min"], "B": "sum"}))
    """
                 A         B
    mean  0.414953       NaN
    min  -1.146306       NaN
    sum        NaN -0.412294
    """

    from functools import partial
    q_25 = partial(pd.Series.quantile, q=0.25)
    print(q_25)
    # functools.partial(<function Series.quantile at 0x000002535DFD6700>, q=0.25)
    q_25.__name__ = "25%"
    print(q_25)
    # functools.partial(<function Series.quantile at 0x00000196FA3D5700>, q=0.25)
    q_75 = partial(pd.Series.quantile, q=0.75)
    print(q_75)
    # functools.partial(<function Series.quantile at 0x00000196FA3D5700>, q=0.75)
    q_75.__name__ = "75%"
    print(q_75)
    # functools.partial(<function Series.quantile at 0x00000196FA3D5700>, q=0.75)
    print(tsdf.agg(["count", "mean", "std", "min", q_25, "median", q_75, "max"]))
    """
                   A         B         C
    count   6.000000  6.000000  6.000000
    mean   -0.429727 -0.647030 -0.474242
    std     0.546310  1.527088  1.592945
    min    -1.158971 -2.128866 -3.301325
    25%    -0.754899 -1.695199 -0.972200
    median -0.321161 -1.133866 -0.024115
    75%    -0.295825  0.104681  0.676285
    max     0.409791  1.879198  0.882579
    """

    # Transform API

    tsdf = pd.DataFrame(
        np.random.randn(10, 3),
        columns=["A", "B", "C"],
        index=pd.date_range("1/1/2000", periods=10),
    )
    print("AAAAAAA")
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.676548 -0.408715 -0.353304
    2000-01-02 -1.397791 -0.339101  0.095091
    2000-01-03 -0.758326  0.114070  1.743653
    2000-01-04 -2.362955  0.166238 -0.744760
    2000-01-05 -0.819081  0.931030 -1.092895
    2000-01-06  0.484775 -2.228617 -0.458651
    2000-01-07 -0.451104  0.691581  0.038731
    2000-01-08 -0.884363 -0.622746 -0.670576
    2000-01-09  1.932779  1.239986 -2.633121
    2000-01-10 -1.634057  1.094748 -0.032573
    """
    print("BBBBBBB")
    tsdf.iloc[3:7] = np.nan
    print(tsdf)
    """
                       A         B         C
    2000-01-01  0.676548 -0.408715 -0.353304
    2000-01-02 -1.397791 -0.339101  0.095091
    2000-01-03 -0.758326  0.114070  1.743653
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08 -0.884363 -0.622746 -0.670576
    2000-01-09  1.932779  1.239986 -2.633121
    2000-01-10 -1.634057  1.094748 -0.032573
    """
    print("CCCCCCC")
    print(tsdf.transform(np.abs))
    """
                   A         B         C
    2000-01-01  0.676548  0.408715  0.353304
    2000-01-02  1.397791  0.339101  0.095091
    2000-01-03  0.758326  0.114070  1.743653
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  0.884363  0.622746  0.670576
    2000-01-09  1.932779  1.239986  2.633121
    2000-01-10  1.634057  1.094748  0.032573
    """
    print(tsdf.transform("abs"))
    """
                   A         B         C
    2000-01-01  0.676548  0.408715  0.353304
    2000-01-02  1.397791  0.339101  0.095091
    2000-01-03  0.758326  0.114070  1.743653
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  0.884363  0.622746  0.670576
    2000-01-09  1.932779  1.239986  2.633121
    2000-01-10  1.634057  1.094748  0.032573
    """
    print(tsdf.transform(lambda x: x.abs()))
    """
                   A         B         C
    2000-01-01  0.676548  0.408715  0.353304
    2000-01-02  1.397791  0.339101  0.095091
    2000-01-03  0.758326  0.114070  1.743653
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  0.884363  0.622746  0.670576
    2000-01-09  1.932779  1.239986  2.633121
    2000-01-10  1.634057  1.094748  0.032573
    """
    print(np.abs(tsdf))
    """
                       A         B         C
    2000-01-01  0.676548  0.408715  0.353304
    2000-01-02  1.397791  0.339101  0.095091
    2000-01-03  0.758326  0.114070  1.743653
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  0.884363  0.622746  0.670576
    2000-01-09  1.932779  1.239986  2.633121
    2000-01-10  1.634057  1.094748  0.032573
    """
    print(tsdf["A"].transform(np.abs))
    """
    2000-01-01    0.676548
    2000-01-02    1.397791
    2000-01-03    0.758326
    2000-01-04         NaN
    2000-01-05         NaN
    2000-01-06         NaN
    2000-01-07         NaN
    2000-01-08    0.884363
    2000-01-09    1.932779
    2000-01-10    1.634057
    Freq: D, Name: A, dtype: float64
    """

    # Transform with multiple functions
    print(tsdf.transform([np.abs, lambda x: x + 1]))
    """
                       A                   B                   C          
            absolute  <lambda>  absolute  <lambda>  absolute  <lambda>
    2000-01-01  0.021835  0.978165  0.310336  0.689664  0.292781  0.707219
    2000-01-02  0.986483  1.986483  1.436247 -0.436247  0.098861  0.901139
    2000-01-03  0.658458  0.341542  0.836060  1.836060  0.083746  1.083746
    2000-01-04       NaN       NaN       NaN       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN       NaN       NaN       NaN
    2000-01-08  0.954146  0.045854  0.598879  1.598879  0.460068  1.460068
    2000-01-09  0.442503  1.442503  0.392153  1.392153  0.291779  0.708221
    2000-01-10  0.107705  1.107705  0.690570  0.309430  0.621091  0.378909
    """
    print(tsdf["A"].transform([np.abs, lambda x: x + 1]))
    """
                absolute  <lambda>
    2000-01-01  0.021835  0.978165
    2000-01-02  0.986483  1.986483
    2000-01-03  0.658458  0.341542
    2000-01-04       NaN       NaN
    2000-01-05       NaN       NaN
    2000-01-06       NaN       NaN
    2000-01-07       NaN       NaN
    2000-01-08  0.954146  0.045854
    2000-01-09  0.442503  1.442503
    2000-01-10  0.107705  1.107705
    """

    # Transforming with a dict
    print(tsdf.transform({"A": np.abs, "B": lambda x: x + 1}))
    """
                       A         B
    2000-01-01  0.083834  2.510756
    2000-01-02  0.254917  2.403796
    2000-01-03  1.019387 -0.831980
    2000-01-04       NaN       NaN
    2000-01-05       NaN       NaN
    2000-01-06       NaN       NaN
    2000-01-07       NaN       NaN
    2000-01-08  0.301154  0.532356
    2000-01-09  1.628123  0.864698
    2000-01-10  1.006269  2.570893
    """
    print(tsdf.transform({"A": np.abs, "B": [lambda x: x + 1, "sqrt"]}))
    """
                       A         B          
            absolute  <lambda>      sqrt
    2000-01-01  0.083834  2.510756  1.229128
    2000-01-02  0.254917  2.403796  1.184819
    2000-01-03  1.019387 -0.831980       NaN
    2000-01-04       NaN       NaN       NaN
    2000-01-05       NaN       NaN       NaN
    2000-01-06       NaN       NaN       NaN
    2000-01-07       NaN       NaN       NaN
    2000-01-08  0.301154  0.532356       NaN
    2000-01-09  1.628123  0.864698       NaN
    2000-01-10  1.006269  2.570893  1.253353
    """

    # Applying Elementwise Functions
    df4 = df.copy()
    print(df4)
    """
            one       two     three
    a  2.964014 -0.251779       NaN
    b  1.004627 -0.184456 -0.754091
    c  1.857768  0.471681 -1.217387
    d       NaN -1.593530  0.338559
    """

    def f(x):
        return len(str(x))

    df4["one"].map(f)
    print(df4.map(f))
    """
       one  two  three
    a   17   19      3
    b   18   20     19
    c   17   18     18
    d    3   18     19
    """

    s = pd.Series(
        ["six", "seven", "six", "seven", "six"], index=["a", "b", "c", "d", "e"]
    )
    print(s)
    """
    a      six
    b    seven
    c      six
    d    seven
    e      six
    dtype: object
    """
    t = pd.Series({"six": 6.0, "seven": 7.0})
    print(t)
    """
    six      6.0
    seven    7.0
    dtype: float64
    """
    print(s.map(t))
    """
    a    6.0
    b    7.0
    c    6.0
    d    7.0
    e    6.0
    dtype: float64
    """
    # Reindexing and altering lables
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    print(s)
    """
    dtype: float64
    a   -1.654944
    b   -0.683086
    c    0.854040
    d   -2.642871
    e   -0.377708
    """
    print(s.reindex(["e", "b", "f", "d"]))
    """
    e   -0.377708
    b   -0.683086
    f         NaN
    d   -2.642871
    dtype: float64
    """

    print(df)
    """
            one       two     three
    a -0.246701  0.404355       NaN
    b  1.109151  0.603100 -0.852315
    c  0.756969  0.584355 -0.411050
    d       NaN -0.538962 -1.693599
    """
    print(df.reindex(index=["c", "f", "b"], columns=["three", "two", "one"]))
    """
          three       two       one
    c -0.411050  0.584355  0.756969
    f       NaN       NaN       NaN
    b -0.852315  0.603100  1.109151
    """


    rs = s.reindex(df.index)
    print(df.index)
    """
    Index(['a', 'b', 'c', 'd'], dtype='object')
    """
    print(rs)
    """
    a   -0.715036
    b    0.335346
    c   -0.709870
    d    0.358814
    dtype: float64
    """
    print(rs.index is df.index)
    """
    True
    """

    print(df.reindex(["c", "f", "b"], axis="index"))
    """
            one       two     three
    c -0.735168 -0.540277 -0.074880
    f       NaN       NaN       NaN
    b  0.213767  0.859130  0.368323
    """
    print(df.reindex(["three", "two", "one"], axis="columns"))
    """
          three       two       one
    a       NaN  0.526528  0.318597
    b  0.368323  0.859130  0.213767
    c -0.074880 -0.540277 -0.735168
    d  0.353565  1.463644       NaN
    """

    df2 = df.reindex(["a", "b", "c"], columns=["one", "two"])
    df3 = df2 - df2.mean()
    print(df2)
    """
            one       two
    a -0.918032  2.098177
    b -0.284536 -0.815467
    c  0.246276 -0.131559
    """
    print(df3)
    """
            one       two
    a -0.599268  1.714460
    b  0.034228 -1.199184
    c  0.565040 -0.515276
    """

    print(df.reindex_like(df2))
    """
            one       two
    a -0.460395  0.138970
    b -0.057936  0.276138
    c -0.578373 -1.037628
    """
    """
    join='outer': take the union of the indexes (default)
    join='left': use the calling object’s index   
    join='right': use the passed object’s index
    join='inner': intersect the indexes
    """
    s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
    s1 = s[:4]
    s2 = s[1:]
    print(s1.align(s2))
    """
    (a   -0.555177
    b    1.751495
    c   -0.492894
    d   -0.184678
    e         NaN
    dtype: float64, a         NaN
    b    1.751495
    c   -0.492894
    d   -0.184678
    e    1.813549
    dtype: float64)
    """
    print(s1.align(s2, join="inner"))
    """
    (b    1.751495
    c   -0.492894
    d   -0.184678
    dtype: float64, b    1.751495
    c   -0.492894
    d   -0.184678
    dtype: float64)
    """
    print(s1.align(s2, join="left"))
    """
    (a   -0.555177
    b    1.751495
    c   -0.492894
    d   -0.184678
    dtype: float64, a         NaN
    b    1.751495
    c   -0.492894
    d   -0.184678
    dtype: float64)
    """
    print(df.align(df2, join="inner"))
    """
    (        one       two
    a  1.039014 -0.010204
    b -0.503466  0.985090
    c  0.042270  1.778703,         one       two
    a  1.039014 -0.010204
    b -0.503466  0.985090
    c  0.042270  1.778703)
    """
    print(df.align(df2, join="inner", axis=0))
    """
    (        one       two     three
    a  1.039014 -0.010204       NaN
    b -0.503466  0.985090 -1.552139
    c  0.042270  1.778703  1.527076,         one       two
    a  1.039014 -0.010204
    b -0.503466  0.985090
    c  0.042270  1.778703)
    """
    print(df.align(df2.iloc[0], axis=1))
    """
    (        one     three       two
    a  1.039014       NaN -0.010204
    b -0.503466 -1.552139  0.985090
    c  0.042270  1.527076  1.778703
    d       NaN  1.486602 -0.927720, one      1.039014
    three         NaN
    two     -0.010204
    Name: a, dtype: float64)
    """

    # Filling while reindexing
    """
    Method            Action
    pad / ffill       Fill values forward
    bfill / backfill  Fill values backward
    nearest           Fill from the nearest index value
    """

    rng = pd.date_range("1/3/2000", periods=8)
    ts = pd.Series(np.random.randn(8), index=rng)
    ts2 = ts.iloc[[0, 3, 6]]
    print(rng)
    """
    DatetimeIndex(['2000-01-03', '2000-01-04', '2000-01-05', '2000-01-06',
               '2000-01-07', '2000-01-08', '2000-01-09', '2000-01-10'],
              dtype='datetime64[ns]', freq='D')
    """
    print(ts)
    """
    2000-01-03   -0.181551
    2000-01-04    1.200444
    2000-01-05    1.377061
    2000-01-06   -0.552844
    2000-01-07   -1.005923
    2000-01-08    0.480494
    2000-01-09   -1.309691
    2000-01-10    2.148627
    Freq: D, dtype: float64
    """
    print(ts2)
    """
    2000-01-03   -0.181551
    2000-01-06   -0.552844
    2000-01-09   -1.309691
    Freq: 3D, dtype: float64
    """
    print(ts2.reindex(ts.index))
    """
    2000-01-03   -0.181551
    2000-01-04         NaN
    2000-01-05         NaN
    2000-01-06   -0.552844
    2000-01-07         NaN
    2000-01-08         NaN
    2000-01-09   -1.309691
    2000-01-10         NaN
    Freq: D, dtype: float64
    """
    print(ts2.reindex(ts.index, method="ffill"))
    """
    2000-01-03   -0.181551
    2000-01-04   -0.181551
    2000-01-05   -0.181551
    2000-01-06   -0.552844
    2000-01-07   -0.552844
    2000-01-08   -0.552844
    2000-01-09   -1.309691
    2000-01-10   -1.309691
    Freq: D, dtype: float64
    """
    print(ts2.reindex(ts.index, method="bfill"))
    """
    2000-01-03   -0.181551
    2000-01-04   -0.552844
    2000-01-05   -0.552844
    2000-01-06   -0.552844
    2000-01-07   -1.309691
    2000-01-08   -1.309691
    2000-01-09   -1.309691
    2000-01-10         NaN
    Freq: D, dtype: float64
    """
    print(ts2.reindex(ts.index, method="nearest"))
    """
    2000-01-03   -0.181551
    2000-01-04   -0.181551
    2000-01-05   -0.552844
    2000-01-06   -0.552844
    2000-01-07   -0.552844
    2000-01-08   -1.309691
    2000-01-09   -1.309691
    2000-01-10   -1.309691
    Freq: D, dtype: float64
    """
    print(ts2.reindex(ts.index).ffill())
    """
    2000-01-03   -0.181551
    2000-01-04   -0.181551
    2000-01-05   -0.181551
    2000-01-06   -0.552844
    2000-01-07   -0.552844
    2000-01-08   -0.552844
    2000-01-09   -1.309691
    2000-01-10   -1.309691
    Freq: D, dtype: float64
    """

    # Limits on filing while reindexing
    print(ts2.reindex(ts.index, method="ffill", limit=1))
    """
    2000-01-03    0.385475
    2000-01-04    0.385475
    2000-01-05         NaN
    2000-01-06   -0.466766
    2000-01-07   -0.466766
    2000-01-08         NaN
    2000-01-09    0.279654
    2000-01-10    0.279654
    Freq: D, dtype: float64
    """
    print(ts2.reindex(ts.index, method="ffill", tolerance="1 day"))
    """
    2000-01-03    0.385475
    2000-01-04    0.385475
    2000-01-05         NaN
    2000-01-06   -0.466766
    2000-01-07   -0.466766
    2000-01-08         NaN
    2000-01-09    0.279654
    2000-01-10    0.279654
    Freq: D, dtype: float64
    """
    print(df)
    """
            one       two     three
    a -0.391287 -0.124559       NaN
    b  0.284193 -0.365877 -1.643898
    c -0.358068 -0.384089 -0.369351
    d       NaN  2.629405  0.514712
    """
    print(df.drop(["a", "d"], axis=0))
    """
            one       two     three
    b  0.284193 -0.365877 -1.643898
    c -0.358068 -0.384089 -0.369351
    """
    print(df.drop(["one"], axis=1))
    """
            two     three
    a -0.124559       NaN
    b -0.365877 -1.643898
    c -0.384089 -0.369351
    d  2.629405  0.514712
    """
    print(df.reindex(df.index.difference(["a", "d"])))
    """
            one       two     three
    b  0.284193 -0.365877 -1.643898
    c -0.358068 -0.384089 -0.369351
    """
    # Renaming/mapping lables
    print(s)
    """
    a   -0.731898
    b   -1.203364
    c    0.119574
    d    1.317053
    e   -0.521152
    dtype: float64
    """
    print(s.rename(str.upper))
    """
    A   -0.731898
    B   -1.203364
    C    0.119574
    D    1.317053
    E   -0.521152
    dtype: float64
    """
    print(df.rename(
        columns={"one": "foo", "two": "bar"},
        index={"a": "apple", "b": "banana", "d": "durian"},
    ))
    """
                 foo       bar     three
    apple  -1.583856 -0.385333       NaN
    banana  0.799485  0.631618  0.208122
    c      -0.565486  0.948278  1.741874
    durian       NaN  0.342362  0.148508
    """
    print(df.rename({"one": "foo", "two": "bar"}, axis="columns"))
    """
            foo       bar     three
    a -1.583856 -0.385333       NaN
    b  0.799485  0.631618  0.208122
    c -0.565486  0.948278  1.741874
    d       NaN  0.342362  0.148508
    """
    print(df.rename({"a": "apple", "b": "banana", "d": "durian"}, axis="index"))
    """
                 one       two     three
    apple  -0.620834  0.523375       NaN
    banana -0.718620  1.307796 -1.158241
    c      -1.168686  2.672840 -1.624455
    durian       NaN  0.540313  0.763776
    """
    print(s.rename("scalar-name"))
    """
    a   -0.973264
    b   -2.548936
    c    0.167584
    d    0.640738
    e   -0.966094
    Name: scalar-name, dtype: float64
    """
    df = pd.DataFrame(
        {"x": [1, 2, 3, 4, 5, 6], "y": [10, 20, 30, 40, 50, 60]},
        index=pd.MultiIndex.from_product(
            [["a", "b", "c"], [1, 2]], names=["let", "num"]
        ),
    )

    print(df)
    """
             x   y
    let num       
    a   1    1  10
        2    2  20
    b   1    3  30
        2    4  40
    c   1    5  50
        2    6  60
    """
    print(df.rename_axis(index={"let": "abc"}))
    """
             x   y
    abc num       
    a   1    1  10
        2    2  20
    b   1    3  30
        2    4  40
    c   1    5  50
        2    6  60
    """
    print(df.rename_axis(index=str.upper))
    """
             x   y
    LET NUM       
    a   1    1  10
        2    2  20
    b   1    3  30
        2    4  40
    c   1    5  50
        2    6  60
    """

    # Iteration

    df = pd.DataFrame(
        {"col1": np.random.randn(3), "col2": np.random.randn(3)}, index=["a", "b", "c"]
    )
    print(df)
    """
           col1      col2
    a -1.337489  0.842319
    b -0.295238  2.207091
    c  0.163497 -1.463298
    """
    for col in df:
        print(col)
    """
    col1
    col2
    """

    for label, ser in df.items():
        print(label)
        print(ser)

    """
    col1
    a    0.067914
    b    1.508864
    c   -0.170268
    Name: col1, dtype: float64
    col2
    a    1.006858
    b   -0.709918
    c    0.276025
    Name: col2, dtype: float64
    """
    for row_index, row in df.iterrows():
        print(row_index, row, sep="\n")
    """
    a
    col1    1.302976
    col2    0.309276
    Name: a, dtype: float64
    b
    col1   -0.698630
    col2    2.357617
    Name: b, dtype: float64
    c
    col1   -0.656755
    col2    1.146545
    Name: c, dtype: float64
    """

    df_orig = pd.DataFrame([[1, 1.5]], columns=["int", "float"])
    print(df_orig.dtypes)
    """
    int        int64
    float    float64
    dtype: object
    """
    row = next(df_orig.iterrows())[1]
    print(row)
    """
    int      1.0
    float    1.5
    Name: 0, dtype: float64
    """
    print(row["int"].dtype)
    """
    float64
    """
    print(df_orig["int"].dtype)
    """
    int64
    """
    df2 = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
    print(df2)
    """
       x  y
    0  1  4
    1  2  5
    2  3  6
    """
    print(df2.T)
    """
       0  1  2
    x  1  2  3
    y  4  5  6
    """
    df2_t = pd.DataFrame({idx: values for idx, values in df2.iterrows()})
    print(df2_t)
    """
       0  1  2
    x  1  2  3
    y  4  5  6
    """
    # itertuples
    print(df)
    """
           col1      col2
    a -0.878392  0.539217
    b  0.591740  0.415494
    c -2.365257 -0.019808
    """
    for row in df.itertuples():
        print(row)
    """
    Pandas(Index='a', col1=-0.4748059746552141, col2=2.4778254311277617)
    Pandas(Index='b', col1=-1.9076905083297517, col2=-1.8066480469250807)
    Pandas(Index='c', col1=-1.7389407237773242, col2=0.17069639892850966)
    """

    s = pd.Series(pd.date_range("20130101 09:10:12", periods=4))
    print(s)
    """
    0   2013-01-01 09:10:12
    1   2013-01-02 09:10:12
    2   2013-01-03 09:10:12
    3   2013-01-04 09:10:12
    dtype: datetime64[ns]
    """
    print(s.dt.hour)
    """
    0    9
    1    9
    2    9
    3    9
    dtype: int32
    """
    print(s.dt.second)
    """
    0    12
    1    12
    2    12
    3    12
    dtype: int32
    """
    print(s.dt.day)
    """
    0    1
    1    2
    2    3
    3    4
    dtype: int32
    """
    print(s[s.dt.day == 2])
    """
    1   2013-01-02 09:10:12
    dtype: datetime64[ns]
    """

    stz = s.dt.tz_localize("US/Eastern")
    print(stz.dt.tz)
    """
    US/Eastern
    """
    print(s.dt.tz_localize("UTC").dt.tz_convert("US/Eastern"))
    """
    0   2013-01-01 04:10:12-05:00
    1   2013-01-02 04:10:12-05:00
    2   2013-01-03 04:10:12-05:00
    3   2013-01-04 04:10:12-05:00
    dtype: datetime64[ns, US/Eastern]
    """
    s = pd.Series(pd.date_range("20130101", periods=4))
    print(s)
    """
    0   2013-01-01
    1   2013-01-02
    2   2013-01-03
    3   2013-01-04
    dtype: datetime64[ns]
    """
    print(s.dt.strftime("%Y/%m/%d"))
    """
    0    2013/01/01
    1    2013/01/02
    2    2013/01/03
    3    2013/01/04
    dtype: object
    """
    s = pd.Series(pd.period_range("20130101", periods=4))
    print(s)
    """
    0    2013-01-01
    1    2013-01-02
    2    2013-01-03
    3    2013-01-04
    dtype: period[D]
    """
    print(s.dt.strftime("%Y/%m/%d"))
    """
    0    2013/01/01
    1    2013/01/02
    2    2013/01/03
    3    2013/01/04
    dtype: object
    """
    s = pd.Series(pd.period_range("20130101", periods=4, freq="D"))
    print(s)
    """
    0    2013-01-01
    1    2013-01-02
    2    2013-01-03
    3    2013-01-04
    dtype: period[D]
    """
    print(s.dt.year)
    """
    0    2013
    1    2013
    2    2013
    3    2013
    dtype: int64
    """
    print(s.dt.day)
    """
    0    1
    1    2
    2    3
    3    4
    dtype: int64
    """
    s = pd.Series(pd.timedelta_range("1 day 00:00:05", periods=4, freq="s"))
    print(s)
    """
    0   1 days 00:00:05
    1   1 days 00:00:06
    2   1 days 00:00:07
    3   1 days 00:00:08
    dtype: timedelta64[ns]
    """
    print(s.dt.days)
    """
    0    1
    1    1
    2    1
    3    1
    dtype: int64
    """
    print(s.dt.seconds)
    """
    0    5
    1    6
    2    7
    3    8
    dtype: int32
    """
    print(s.dt.components)
    """
       days  hours  minutes  seconds  milliseconds  microseconds  nanoseconds
    0     1      0        0        5             0             0            0
    1     1      0        0        6             0             0            0
    2     1      0        0        7             0             0            0
    3     1      0        0        8             0             0            0
    """

    s = pd.Series(
        ["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"], dtype="string"
    )
    print(s)
    """
    0       A
    1       B
    2       C
    3    Aaba
    4    Baca
    5    <NA>
    6    CABA
    7     dog
    8     cat
    dtype: string
    """
    print(s.str.lower())
    """
    0       a
    1       b
    2       c
    3    aaba
    4    baca
    5    <NA>
    6    caba
    7     dog
    8     cat
    dtype: string
    """

    # Sorting
    # By Index
    df = pd.DataFrame(
        {
            "one": pd.Series(np.random.randn(3), index=["a", "b", "c"]),
            "two": pd.Series(np.random.randn(4), index=["a", "b", "c", "d"]),
            "three": pd.Series(np.random.randn(3), index=["b", "c", "d"]),
        }
    )

    unsorted_df = df.reindex(
        index=["a", "d", "c", "b"], columns=["three", "two", "one"]
    )
    print(unsorted_df)
    """
          three       two       one
    a       NaN -1.405833 -0.049031
    d  0.310895 -0.562564       NaN
    c -0.171565  0.772711 -0.772859
    b -1.407299  0.049214 -1.368722
    """
    print(unsorted_df.sort_index())
    """
          three       two       one
    a       NaN -1.405833 -0.049031
    b -1.407299  0.049214 -1.368722
    c -0.171565  0.772711 -0.772859
    d  0.310895 -0.562564       NaN
    """
    print(unsorted_df.sort_index(ascending=False))
    """
          three       two       one
    d  0.310895 -0.562564       NaN
    c -0.171565  0.772711 -0.772859
    b -1.407299  0.049214 -1.368722
    a       NaN -1.405833 -0.049031
    """
    print(unsorted_df.sort_index(axis=1))
    """
            one     three       two
    a -0.049031       NaN -1.405833
    d       NaN  0.310895 -0.562564
    c -0.772859 -0.171565  0.772711
    b -1.368722 -1.407299  0.049214
    """
    print(unsorted_df["three"].sort_index())
    """
    a         NaN
    b   -1.407299
    c   -0.171565
    d    0.310895
    Name: three, dtype: float64
    """
    s1 = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3], "c": [2, 3, 4]}).set_index(
        list("ab")
    )
    print(s1)
    """
         c
    a b   
    B 1  2
    a 2  3
    C 3  4
    """
    print(s1.sort_index(level="a"))
    """
         c
    a b   
    B 1  2
    C 3  4
    a 2  3
    """
    print(s1.sort_index(level="a", key=lambda idx: idx.str.lower()))
    """
         c
    a b   
    a 2  3
    B 1  2
    C 3  4
    """
    # By values
    df1 = pd.DataFrame(
        {"one": [2, 1, 1, 1], "two": [1, 3, 2, 4], "three": [5, 4, 3, 2]}
    )
    print(df1.sort_values(by="two"))
    print(df1[["one", "two", "three"]].sort_values(by=["one", "two"]))
    """
       one  two  three
    0    2    1      5
    2    1    2      3
    1    1    3      4
    3    1    4      2
    """
    s[2] = np.nan
    print(s.sort_values())
    """
       one  two  three
    2    1    2      3
    1    1    3      4
    3    1    4      2
    0    2    1      5
    """
    print(s.sort_values(na_position="first"))
    """
    0       A
    3    Aaba
    1       B
    4    Baca
    6    CABA
    8     cat
    7     dog
    2    <NA>
    5    <NA>
    dtype: string
    """
    s1 = pd.Series(["B", "a", "C"])
    print(s1.sort_values())
    """
    2    <NA>
    5    <NA>
    0       A
    3    Aaba
    1       B
    4    Baca
    6    CABA
    8     cat
    7     dog
    dtype: string
    """
    print(s1.sort_values(key=lambda x: x.str.lower()))
    """
    0    B
    2    C
    1    a
    dtype: object
    """
    df = pd.DataFrame({"a": ["B", "a", "C"], "b": [1, 2, 3]})
    print(df.sort_values(by="a"))
    """
    1    a
    0    B
    2    C
    dtype: object
    """
    print(df.sort_values(by="a", key=lambda col: col.str.lower()))
    """
       a  b
    0  B  1
    2  C  3
    1  a  2
       a  b
    1  a  2
    0  B  1
    2  C  3
    """

    # By indexes and values
    idx = pd.MultiIndex.from_tuples(
        [("a", 1), ("a", 2), ("a", 2), ("b", 2), ("b", 1), ("b", 1)]
    )
    idx.names = ["first", "second"]
    print(idx)
    """
    MultiIndex([('a', 1),
            ('a', 2),
            ('a', 2),
            ('b', 2),
            ('b', 1),
            ('b', 1)],
           names=['first', 'second'])
    """
    df_multi = pd.DataFrame({"A": np.arange(6, 0, -1)}, index=idx)
    print(df_multi)
    """
                  A
    first second   
    a     1       6
          2       5
          2       4
    b     2       3
          1       2
          1       1
                  A
    """
    print(df_multi.sort_values(by=["second", "A"]))
    """
    first second   
    b     1       1
          1       2
    a     1       6
    b     2       3
    a     2       4
          2       5
    """
    ser = pd.Series([1, 2, 3])
    print(ser.searchsorted([0, 3]))
    """
    [0 2]
    """
    print(ser.searchsorted([0, 4]))
    """
    [0 3]
    """
    print(ser.searchsorted([1, 3], side="right"))
    """
    [1 3]
    """
    print(ser.searchsorted([1, 3], side="left"))
    """
    [0 2]
    """
    ser = pd.Series([3, 1, 2])
    print(ser.searchsorted([0, 3], sorter=np.argsort(ser)))
    """
    [0 2]
    """
    # smallest / largest values
    s = pd.Series(np.random.permutation(10))
    print(s)
    """
    0    1
    1    2
    2    7
    3    3
    4    8
    5    9
    6    5
    7    0
    8    4
    9    6
    dtype: int32
    """
    print(s.sort_values())
    """
    7    0
    0    1
    1    2
    3    3
    8    4
    6    5
    9    6
    2    7
    4    8
    5    9
    dtype: int32
    """
    print(s.nsmallest(3))
    """
    7    0
    0    1
    1    2
    dtype: int32
    """
    print(s.nlargest(3))
    """
    5    9
    4    8
    2    7
    dtype: int32
    """
    df = pd.DataFrame(
        {
            "a": [-2, -1, 1, 10, 8, 11, -1],
            "b": list("abdceff"),
            "c": [1.0, 2.0, 4.0, 3.2, np.nan, 3.0, 4.0],
        }
    )
    print(df.nlargest(3, "a"))
    """
        a  b    c
    5  11  f  3.0
    3  10  c  3.2
    4   8  e  NaN
    """
    print(df.nlargest(5, ["a", "c"]))
    """
        a  b    c
    5  11  f  3.0
    3  10  c  3.2
    4   8  e  NaN
    2   1  d  4.0
    6  -1  f  4.0
    """
    print(df.nsmallest(3, "a"))
    """
       a  b    c
    0 -2  a  1.0
    1 -1  b  2.0
    6 -1  f  4.0
    """
    print("AAAAAAAA")
    print(df.nsmallest(5, ["a", "c"]))
    """
       a  b    c
    0 -2  a  1.0
    1 -1  b  2.0
    6 -1  f  4.0
    2  1  d  4.0
    4  8  e  NaN
    """
    # Sorting by a MultiIndex column
    df1.columns = pd.MultiIndex.from_tuples(
        [("a", "one"), ("a", "two"), ("b", "three")]
    )
    print(df1.sort_values(by=("a", "two")))
    """
        a         b
      one two three
    0   2   1     5
    2   1   2     3
    1   1   3     4
    3   1   4     2
    """

    #Copying
    """
    Kind of Data             Data Type        Scalar        Array                    String Aliases
    tz-aware datetime        DatetimeTZDtype  Timestamp     arrays.DatetimeArray     'datetime64[ns, <tz>]'
    Categorical              CategoricalDtype (none)        Categorical              'category'
    period (time spans)      PeriodDtype      Period        arrays.PeriodArray 
                                                            'Period[<freq>]'         'period[<freq>]',
    sparse                   SparseDtype      (none)        arrays.SparseArray       'Sparse', 'Sparse[int]', 
                                                                                     'Sparse[float]'
    intervals                IntervalDtype    Interval      arrays.IntervalArray     'interval', 'Interval', 
                                                                                     'Interval[<numpy_dtype>]', 
                                                                                     'Interval[datetime64[ns, <tz>]]', 
                                                                                     'Interval[timedelta64[<freq>]]'
    nullable integer         Int64Dtype, …    (none)        arrays.IntegerArray      'Int8', 'Int16', 'Int32', 'Int64', 
                                                                                     'UInt8','UInt16','UInt32','UInt64'
    nullable float           Float64Dtype, …  (none)        arrays.FloatingArray     'Float32', 'Float64'
    Strings                  StringDtype      str           arrays.StringArray       'string'
    Boolean (with NA)        BooleanDtype     bool          arrays.BooleanArray      'boolean'
    """

    dft = pd.DataFrame(
        {
            "A": np.random.rand(3),
            "B": 1,
            "C": "foo",
            "D": pd.Timestamp("20010102"),
            "E": pd.Series([1.0] * 3).astype("float32"),
            "F": False,
            "G": pd.Series([1] * 3, dtype="int8"),
        }
    )

    print(dft)
    print(dft.dtypes)
    print(dft["A"].dtype)
    print(pd.Series([1, 2, 3, 4, 5, 6.0]))
    print(pd.Series([1, 2, 3, 6.0, "foo"]))
    print(dft.dtypes.value_counts())

    df1 = pd.DataFrame(np.random.randn(8, 1), columns=["A"], dtype="float32")
    print(df1)
    print(df1.dtypes)
    df2 = pd.DataFrame(
        {
            "A": pd.Series(np.random.randn(8), dtype="float16"),
            "B": pd.Series(np.random.randn(8)),
            "C": pd.Series(np.random.randint(0, 255, size=8), dtype="uint8"),  # [0,255] (range of uint8)
        }
    )

    print(df2)
    print(df2.dtypes)


essential_basic_functionality()