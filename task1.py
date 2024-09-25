import math

x = float(input("Уведіть аргумент: "))
y = 0.0

if x >= 5.1:
    y = math.log(2, 3*x) - 7 * math.sqrt(x) 
elif -0.7 < x < 5.1:
    y = math.exp(x) + 2*x**3
else:
    y = math.exp(x) + math.sin(x + math.pi/4)

print("y=", y)
