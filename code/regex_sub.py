import re
reg_and = r"\s\&\&\s"
reg_or = r"\s\|\|\s"
n = 11
ss = ["aaa && bbb || ccc"]
ss = ["x&& &&& && && x || | ||\|| x"]
ss = ["c $&1|| || && && &|&&| & | | &&c"]

ss = ['n && && && && && &&n']

for s in ss:
    s = s.rstrip()
    s2 = ""
    s3 = ""
    if ' && ' in s:
        while ' && ' in s:
            s = re.sub(reg_and, " and ", s)
    if ' || ' in s:
        while ' || ' in s2:
            s = re.sub(reg_or, " or ", s)
        print(s)
    else:
        print(s)