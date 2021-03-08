from shape import Triangle, Square, Circle

a = input("1. Triangle \n2. Square \n3. Circle\n")
c = input("details: ")
d = c.split()
b = []
for x in d:
    b.append(int(x))
if a == '1':
    s = Triangle(b[0], b[1])
elif a == '2':
    s = Square(b[0])
else:
    s = Circle(b[0])
s.area()
s.perimeter()


