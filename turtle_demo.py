import turtle

t = turtle.Turtle()
#t.forward(50)
#t.left
#t.circle(60)

for i in range(100):
    t.forward(i)
    t.left(15)

turtle.mainloop()