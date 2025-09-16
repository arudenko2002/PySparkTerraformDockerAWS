import pandas as pd
import pyarrow as pa

# Structure Integration
def structure_integration():
    ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
    print(ser)
    # 0    -1.5
    # 1     0.2
    # 2    <NA>
    # dtype: float[pyarrow]
    idx = pd.Index([True, None], dtype="bool[pyarrow]")
    print(idx)
    # Index([True, <NA>], dtype='bool[pyarrow]')
    df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
    print(df)
    #    0  1
    # 0  1  2
    # 1  3  4
    data = list("abc")
    print(data)
    # ['a', 'b', 'c']
    ser_sd = pd.Series(data, dtype="string[pyarrow]")
    print(ser_sd)
    """
    0    a
    1    b
    2    c
    dtype: string
    """
    ser_ad = pd.Series(data, dtype=pd.ArrowDtype(pa.string())) # ser_ad.dtype NOT SAME AS ser_sd.dtype
    print(ser_ad)
    """
    0    a
    1    b
    2    c
    dtype: string[pyarrow]
    """
    print(ser_sd.str.contains("a"))
    """
    0     True
    1    False
    2    False
    dtype: boolean
    """
    print(ser_ad.str.contains("a"))
    """
    0     True
    1    False
    2    False
    dtype: bool[pyarrow]
    """
    list_str_type = pa.list_(pa.string())
    ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
    print(ser)
    """
    0    ['hello']
    1    ['there']
    dtype: list<item: string>[pyarrow]
    """

    from datetime import time
    idx = pd.Index([time(12, 30), None], dtype=pd.ArrowDtype(pa.time64("us")))
    print(idx)
    # Index([12:30:00, <NA>], dtype='time64[us][pyarrow]')

    from decimal import Decimal
    decimal_type = pd.ArrowDtype(pa.decimal128(3, scale=2))
    print(pa.decimal128(3, scale=2))
    # decimal128(3, 2)
    data = [[Decimal("3.19"), None], [None, Decimal("-1.23")]]
    df = pd.DataFrame(data, dtype=decimal_type)
    print(df)
    """
          0      1
    0  3.19   <NA>
    1  <NA>  -1.23
    """

    pa_array = pa.array(
        [{"1": "2"}, {"10": "20"}, None],
        type=pa.map_(pa.string(), pa.string()),
    )
    ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
    print(ser)
    """
    0      [('1', '2')]
    1    [('10', '20')]
    2              <NA>
    dtype: map<string, string>[pyarrow]
    """

    ser = pd.Series([1, 2, None], dtype="uint8[pyarrow]")
    print(pa.array(ser))
    """
    [
      1,
      2,
      null
    ]
    """

    idx = pd.Index(ser)
    print(pa.array(idx))
    """
    [
      1,
      2,
      null
    ]
    """

    table = pa.table([pa.array([1, 2, 3], type=pa.int64())], names=["a"])
    print(table)
    """
    pyarrow.Table
    a: int64
    ----
    a: [[1,2,3]]
    """
    df = table.to_pandas(types_mapper=pd.ArrowDtype)
    print(df)
    """
       a
    0  1
    1  2
    2  3
    """

structure_integration()

def operations():
    ser = pd.Series([-1.545, 0.211, None], dtype="float32[pyarrow]")
    print(ser)
    """
    0   -1.545
    1    0.211
    2     <NA>
    dtype: float[pyarrow]
    """
    print(ser.mean())
    # -0.6669999808073044
    ser2 = ser + ser
    print(ser2)
    """
    0    -3.09
    1    0.422
    2     <NA>
    dtype: float[pyarrow]
    """
    print(ser > (ser + 1))
    """
    0    False
    1    False
    2     <NA>
    dtype: bool[pyarrow]
    """
    print(ser.dropna())
    """
    0   -1.545
    1    0.211
    dtype: float[pyarrow]
    """
    print(ser.isna())
    """
    0    False
    1    False
    2     True
    dtype: bool
    """
    print(ser.fillna(0))
    """
    0   -1.545
    1    0.211
    2      0.0
    dtype: float[pyarrow]
    """

    ser_str = pd.Series(["a", "b", None], dtype=pd.ArrowDtype(pa.string()))
    print(ser_str.str.startswith("a"))
    """
    0     True
    1    False
    2     <NA>
    dtype: bool[pyarrow]
    """

    from datetime import datetime
    pa_type = pd.ArrowDtype(pa.timestamp("ns"))
    print(pa_type)
    # timestamp[ns][pyarrow]
    ser_dt = pd.Series([datetime(2022, 1, 1), None], dtype=pa_type)
    print(ser_dt)
    """
    0    2022-01-01 00:00:00
    1                   <NA>
    dtype: timestamp[ns][pyarrow]
    """
    # print(ser_dt.dt.strftime("%Y-%m"))
    # not working: pyarrow.lib.ArrowInvalid: Cannot locate timezone 'UTC': Timezone database not found at
    # "C:\Users\AlexR\Downloads\tzdata"
    """
    0    2022-01
    1       <NA>
    dtype: string[pyarrow]
    """

operations()

def io_reading():
    import io
    data = io.StringIO(
"""
a,b,c
1,2.5,True
3,4.5,False
""")
    print(data)
    # <_io.StringIO object at 0x0000022967513790>
    df = pd.read_csv(data, engine="pyarrow", sep=",")
    print(df)
    """
       a    b      c
    0  1  2.5   True
    1  3  4.5  False
    """
    data = io.StringIO("""a,b,c,d,e,f,g,h,i
        1,2.5,True,a,,,,,
        3,4.5,False,b,6,7.5,True,a,
    """)
    df_pyarrow = pd.read_csv(data, dtype_backend="pyarrow")
    print(df_pyarrow.dtypes)
    """
a     int64[pyarrow]
b    double[pyarrow]
c      bool[pyarrow]
d    string[pyarrow]
e     int64[pyarrow]
f    double[pyarrow]
g      bool[pyarrow]
h    string[pyarrow]
i      null[pyarrow]
dtype: object
    """

io_reading()

