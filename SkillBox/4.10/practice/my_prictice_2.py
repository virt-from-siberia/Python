import simple_draw as sd

length = 200
point_1 = sd.get_point(300, 300)

poiint_0 = sd.get_point(300, 5)

v1 = sd.get_vector(start_point=poiint_0, angle=90, length=100)
v1.draw()


def triangle(point, angle=0):
    pass


sd.pause()
