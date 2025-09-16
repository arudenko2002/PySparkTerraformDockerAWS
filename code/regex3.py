regex_integer_in_range = r"^[7,8,9][0-9]{9}$"	# Do not delete 'r'.


# (\d): Match and capture a digit in group #1
# (?=: Start lookahead
# \d: Match any digit
# \1: Back-reference to captured group #1
# ): End lookahead

import re

ss = ["7214260100",
"6414129111"]
for p in ss:
    print(bool(re.match(regex_integer_in_range, p)))