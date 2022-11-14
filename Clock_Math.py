h, m = map(int, input().split())
if h > 12 or m > 60 or h < 0 or m < 0:
    print("wrong input")
if h == 12:
    h = 0
if m == 60:
    m = 0
hour_angle = 0.5 * (h * 60 + m)
minute_angle = 6 * m
angle = (hour_angle - minute_angle)
angle = min(360 - angle, angle)
print(angle)
