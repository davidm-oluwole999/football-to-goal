'''replicate the same game with a different image.
create multiple images of path 1 2 3 4 5 6 7 8
create a playerand create a goal
put a background'''


import pgzrun
from random import randint

WIDTH= 800
HEIGHT= 500

satellites= []
lines= []
next_satellite= 0
number_of_satellite= 8

def create_satellites():
    for count in range(0, number_of_satellite):
        satellite= Actor("ball")
        satellite.pos= randint(40, WIDTH-40), randint(40, HEIGHT-40)
        satellites.append(satellite)



def draw():
    screen.blit('pitch',(0,0))
    number=1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0],satellite.pos[1]+20))
        satellite.draw()
        number=number+1




create_satellites()
pgzrun.go()