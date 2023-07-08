from turtle import Turtle, Screen


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
HALL_HEADER = 100

ROW = 10
COLUMN = 10

FONT_SIZE = 18

main_screen = Screen()
main_screen.bgcolor("white")
main_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.setworldcoordinates(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
main_screen.title("Cinema")

main_pen = Turtle()
main_pen.hideturtle()
main_pen.speed(0)
main_pen.up()

write_pen = Turtle()
write_pen.hideturtle()
write_pen.speed(0)
write_pen.up()

write_pen1 = Turtle()
write_pen1.hideturtle()
write_pen1.speed(0)
write_pen1.up()

cell_width = SCREEN_WIDTH / COLUMN
cell_height = (SCREEN_HEIGHT - HALL_HEADER) / ROW

seat_radius = (cell_height * 0.8) / 2

x = cell_width / 2
y = (cell_height / 2) - seat_radius

seats = {}

for r in range(ROW):
    for c in range(COLUMN):
        seats[(x, y)] = False
        x += cell_width
    x = cell_width / 2
    y += cell_height


def draw_screen():
    main_pen.fillcolor("green")
    main_pen.setposition(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
    main_pen.begin_fill()
    main_pen.down()
    main_pen.forward(450)
    main_pen.right(90)
    main_pen.forward(50)
    main_pen.right(90)
    main_pen.forward(900)
    main_pen.right(90)
    main_pen.forward(50)
    main_pen.right(90)
    main_pen.forward(900)
    main_pen.end_fill()
    main_pen.up()


def write_free_seats():
    main_screen.tracer(False)
    write_pen.clear()
    write_pen.setposition(10, SCREEN_HEIGHT - FONT_SIZE * 2)
    write_pen.down()
    free_seats = 0
    for status in seats.values():
        if not status:
            free_seats += 1    
    write_pen.write(f"Free: {free_seats}", font=("Arial", FONT_SIZE, "bold"))
    write_pen.up()
    main_screen.tracer(True)


def write_sold_seats(): 
    main_screen.tracer(False)
    write_pen1.clear()
    write_pen1.setposition(10, SCREEN_HEIGHT - FONT_SIZE * 4)
    write_pen1.down()
    sold_seats = 0
    for status in seats.values():
        if status:
            sold_seats += 1
    write_pen1.write(f"Sold: {sold_seats}", font=("Arial", FONT_SIZE, "bold"))
    write_pen1.up()
    main_screen.tracer(True)

def draw_seat(x, y, color="green"):
    main_pen.setposition(x, y)
    main_pen.down()
    main_pen.begin_fill()
    main_pen.circle(seat_radius)
    main_pen.fillcolor(color)
    main_pen.end_fill()
    main_pen.up()


def get_seat(x, y):
    for seat_x, seat_y in seats:
        distance = ((x - seat_x)**2 + (y - (seat_y + seat_radius))**2)**0.5
        if distance <= seat_radius:
            return seat_x, seat_y
    return None


def on_seat_click(x, y):
    seat = get_seat(x, y)
    if seat:
        seats[seat] = True
        draw_seat(*seat, color="red")
        write_free_seats()
        write_sold_seats()

def on_seat_right_click(x, y): 
    seat = get_seat(x, y)
    if seat:
        seats[seat] = False
        draw_seat(*seat, color="green")
        write_free_seats()     
        write_sold_seats()   

def double_on_seat_click(x, y): 
    seat = get_seat(x, y)
    if seat:
        seats[seat] = False
        draw_seat(*seat, color="blue")    
        write_free_seats() 
        write_sold_seats()   


main_screen.tracer(False)
for seat_x, seat_y in seats:
    draw_seat(seat_x, seat_y)
draw_screen()
write_free_seats()
write_sold_seats()
main_screen.tracer(True)




main_screen.onclick(on_seat_right_click, btn = 3) 
main_screen.onclick(on_seat_click, btn = 1 ) 
main_screen.mainloop()