from turtle import Turtle, Screen


FORWARD_DRAW =200 

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
HALL_HEADER = 100

ROW = 10
COLUMN = 10

main_screen = Screen()
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates (0,0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title('Cinema')

main_pen = Turtle()
main_pen.hideturtle()
main_pen.speed(0)
main_pen.up()

cell_width = SCREEN_WIDTH / COLUMN
cell_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW

seat_radius = (cell_height * 0.8) / 2

x = cell_width / 2
y = (cell_height / 2) - seat_radius

seats = {}

for r in range(ROW):
    for c in range(COLUMN):
        seats[(x,y)] = False
        x += cell_width
    x= cell_width / 2
    y+= cell_height



def draw_screen():
    main_pen.setposition(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
    main_pen.down()
    main_pen.forward(100)
    main_pen.right(90)
    main_pen.forward(30)
    main_pen.right(90)
    main_pen.forward(200)
    main_pen.right(90)
    main_pen.forward(30)
    main_pen.right(90)
    main_pen.forward(100)
    main_pen.up() 

def draw_seat(x, y):
    main_pen.setposition(x,y)
    main_pen.down()
    main_pen.circle(seat_radius)
    main_pen.up()

for seat_x, seat_y in seats:
    draw_seat(seat_x, seat_y)

draw_screen()
# main_pen.setposition(x,y)
# main_pen.down()
# main_pen.circle(seat_radius)
# main_pen.up()

main_screen.mainloop()
