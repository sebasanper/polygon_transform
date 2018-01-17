from transform_quadrilateral import AreaMapping
from random import random, uniform

real1 = [[484178.55, 5732482.8], [500129.9, 5737534.4], [497318.1, 5731880.24], [491858.00, 5725044.75]]
real2 = [[491858.00, 5725044.75], [497318.1, 5731880.24], [503163.37, 5729155.3], [501266.5, 5715990.05]]
transf1 = [[0, 0], [0, 1.0], [0.5, 1.0], [0.5, 0]]
transf2 = [[0.5, 0], [0.5, 1.0], [1.0, 1.0], [1.0, 0]]


squares = []
area = [real1, real2]   
n_quadrilaterals = 2
for n in range(n_quadrilaterals):
    square = [[1.0 / n_quadrilaterals * n, 0.0], [n * 1.0 / n_quadrilaterals, 1.0], [(n + 1) * 1.0 / n_quadrilaterals, 1.0], [(n + 1) * 1.0 / n_quadrilaterals, 0.0]]
    squares.append(square)
borssele_mapping1 = AreaMapping(area[0], squares[0])
borssele_mapping2 = AreaMapping(area[1], squares[1])

# 500129.9    5737534.4   top corner right 1
# 484178.55   5732482.8   left corner 1
# 497318.1    5731880.24  inside corner right 1 and 2
# 503163.37   5729155.3   right corner 2
# 501266.5    5715990.05  bottom corner 2
# 491858.00   5725044.75  middle corner 1 and 2


bx = []
by = []
bz = []
m = (real2[0][1] - real2[1][1]) / (real2[0][0] - real2[1][0])
y = real2[0][1]
x = real2[0][0]
b = y - m * x

def create_random():
    xt, yt = 2.0, 2.0
    while (xt < 0.0 or xt > 1.0) or (yt < 0.0 or yt > 1.0):
        xb, yb = uniform(min(min([item[0] for item in real1]), min([item[0] for item in real2])), max(max([item[0] for item in real1]), max([item[0] for item in real2]))), uniform(min(min([item[1] for item in real1]), min([item[1] for item in real2])), max(max([item[1] for item in real1]), max([item[1] for item in real2])))
        if yb > m * xb + b:
            xt, yt = borssele_mapping1.transform_to_rectangle(xb, yb)
        else:
            xt, yt = borssele_mapping2.transform_to_rectangle(xb, yb)
    return xb, yb

with open("randomness_borssele.dat", "w") as out:
    for _ in range(10000):
        x, y  = random(), random()
        if x < 0.5:
            nx, ny = borssele_mapping1.transform_to_shape(x, y)
        else:
            nx, ny = borssele_mapping2.transform_to_shape(x, y)
        bx, by = create_random()
        out.write("{} {} {} {}\n".format(nx, ny, bx, by))
