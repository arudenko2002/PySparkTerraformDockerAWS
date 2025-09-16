ss = "String1234"
s = sorted(ss)
print(s)
even_digits = sorted(d for d in s if d.isdigit() and int(d) % 2 == 0)
odd_digits = sorted(d for d in s if d.isdigit() and int(d) % 2 != 0)
lower_case = sorted(c for c in ss if c.islower())
upper_case = sorted(c for c in ss if c.isupper())
print(''.join(lower_case+upper_case+odd_digits+even_digits))
