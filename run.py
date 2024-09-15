import sys, main

main.init()

size = width, height = 640, 480
dx = 1
dy = 1
x= 163
y = 120
black = (0,0,0)
white = (255,255,255)

screen = main.display.set_mode(size)

while 1:

    for event in main.event.get():
        if event.type == main.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    screen.fill(black)

    main.draw.circle(screen, white, (x,y), 8)

    main.display.flip()