splip = Actor("character")
splip.pos = 100, 35
WIDTH = 500
HEIGHT = splip.height + 20


def draw():
    screen.fill((255, 0, 0))
    splip.draw()


def update():
    splip.left = splip.left + 2

