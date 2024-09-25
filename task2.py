def check_within_range(min, val, max):
    return min < val < max

a = float(input("Уведіть сторону квадрата: "))
s1x = -a/2
s1y = -a/2
s1z = -a/2

s2x = a/2
s2y = a/2
s2z = a/2

pointStr = input("Уведіть кординати точки як x,y,z:")
cordsStrArr = pointStr.split(",")
px = float(cordsStrArr[0])
py = float(cordsStrArr[1])
pz = float(cordsStrArr[2])

isWithinRangeX = check_within_range(s1x, px, s2x)
isWithinRangeY = check_within_range(s1y, px, s2y)
isWithinRangeZ = check_within_range(s1z, px, s2z)

isWithinRange = isWithinRangeX & isWithinRangeY & isWithinRangeZ

print("Точка (" 
      + "x:" + str(px)
      + ", y:" + str(py)
      + ", z:" + str(pz)
      + ") " 
      + (" є" if isWithinRange else " Не є")
      + " всередині квадрата зі стороною " + str(a))
