s = "bicycle"
print(s[::3]) # bye
print(s[::-1]) #elcycib
print(s[::-2]) #eccb
print(reversed(s)) #<reversed object at 0x0000022743B4FFD0>
rs = reversed(s)
print(''.join(rs))  #elcycib
print(s[:-1]) #bicycl
print(s[-1:]) #e
print(s[:1]) #b
print(s[1:]) #icycle
print('aaa=',s,'bbb',s[:])
