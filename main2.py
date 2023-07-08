from turtle import Turtle, Screen


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
HALL_HEADER = 100

ROW = 10
COLUMN = 10

FONT_SIZE = 18

main_screen = Screen()
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


def write_free_seats():
    main_screen.tracer(False)
    write_pen.clear()
    write_pen.setposition(10, SCREEN_HEIGHT - FONT_SIZE * 2)
    write_pen.down()
    free_seats = len([status for status in seats.values() if not status])
    free_seats = 0
    for status in seats.values():
        if not status:
            free_seats += 1
    write_pen.write(f"Free: {free_seats}", font=("Arial", FONT_SIZE, "bold"))
    write_pen.up()
    main_screen.tracer(True)


def draw_seat(x, y, color="steel blue"):
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
        draw_seat(*seat, color="#00FA9A")
        write_free_seats()


main_screen.tracer(False)
for seat_x, seat_y in seats:
    draw_seat(seat_x, seat_y)
draw_screen()
write_free_seats()
main_screen.tracer(True)



main_screen.onclick(on_seat_click)
main_screen.mainloop()