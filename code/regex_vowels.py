import re
s = 'rabcdeefgyYhFjkIoomnpOeorteeeeet'
s = "match a single character not present in the list below"
s = 'abaabaabaabaae'
reg = r"[AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]"
rez = re.findall(reg, s)
for ind in rez:
    print(ind[:len(ind)-1])