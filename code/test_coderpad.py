ts = [15, -7.1, 9.2, 14.3, 7.1, 12.9]
ts = [15, -7.1, 9.2, 14.3, -7.1, 12.9]
ts = [-15.8, -50.7, 9.6, -14.5, -9.7, 200, -9.6]

dist = max(ts)
print(dist)
rez = dist
for t in ts:
    print('t=',t, 'dist=', dist, 'rez=',rez)
    if abs(t)<=dist:
        dist=abs(t)
        if not (rez==dist and rez>0):
            rez = t
    # if t >= 0 and t <= dist:
    #     dist = t
    # elif t <= 0 and abs(t) < dist:
    #     dist = abs(t)
    # else:
    #     pass

print(rez)