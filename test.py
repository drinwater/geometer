import geometer2 as gx
from datetime import datetime

start = datetime.now()
p = gx.Point(2, 4)
q = gx.Point(3, 5)
l = gx.Line(p, q)
m = gx.Line(0, 1, 0)
end = datetime.now()
print(end - start)