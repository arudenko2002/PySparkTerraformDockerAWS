regex_integer_in_range = r"^[1-9][0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"


# 121426 <- Here, 1 is an alternating repetitive digit.
# 523563 <- Here, NO digit is an alternating repetitive digit.
# 552523 <- Here, both 2 and 5 are alternating repetitive digits.
# 333567 <- Here, 3 is an alternating repetitive digit.

# (\d): Match and capture a digit in group #1
# (?=: Start lookahead
# \d: Match any digit
# \1: Back-reference to captured group #1
# ): End lookahead

import re
#P = input()
P = "121426"
P = "6414129"
P="110000"
P="4542867"
print(bool(re.match(regex_integer_in_range, P)))
print(re.findall(regex_alternating_repetitive_digit_pair, P))
#print(len(re.findall(regex_alternating_repetitive_digit_pair, P)))

print (bool(re.match(regex_integer_in_range, P))
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)