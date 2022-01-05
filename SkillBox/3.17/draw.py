import simple_draw as sd

sd.resolution = (1200, 600)
point = sd.get_point(300, 300)


def bubble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


bubble(point=point, step=10)

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    bubble(point=point, step=5)

for y in range(100, 301, 100):
    for x in range(100, 1001, 100):
        point = sd.get_point(x, y)
        bubble(point=point, step=5)

for _ in range(100):
    point = sd.random_point(x, y)
    bubble(point=point, step=)

sd.pause()
