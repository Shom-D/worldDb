import pgzrun

WIDTH = 300
HEIGHT = 300

def draw():
    screen.clear()
    width=WIDTH
    height=HEIGHT-200
    for x in range(20):
        rectangle = Rect((0,0),(width, height))
        rectangle.center= (150,150)
        screen.draw.rect(rectangle,(255,0,0))
        width -= 10 
        height += 10

pgzrun.go()
