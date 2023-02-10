import time

splip = Actor("character")
splip.pos = 100, 35
WIDTH = 500
HEIGHT = splip.height + 20


def draw():
    screen.fill((180, 0, 0))
    splip.draw()


def update():
    splip.left = splip.left + 2
    if splip.left > WIDTH:
        splip.left = 0

def on_mouse_down(pos):
    if splip.collidepoint(pos):
        set_splip_hurt()
        sounds.eep.play()
def set_splip_hurt():
    splip.image = "character_clicked"
    clock.schedule_unique(set_splip_normal, 1.0)
    print("OHHHHH")
def set_splip_normal():
    splip.image = "character"



