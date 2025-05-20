import turtle
import random

def draw_heart():
    turtle.color('red')
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def draw_ring():
    turtle.color('gold')
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(60)
    turtle.pensize(1)

def draw_flower():
    turtle.color('pink')
    for _ in range(36):
        turtle.begin_fill()
        turtle.circle(50, 60)
        turtle.left(120)
        turtle.circle(50, 60)
        turtle.left(120)
        turtle.end_fill()
        turtle.right(10)


def draw_heart(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(140)
    turtle.forward(size)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(size * 0.011)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(size * 0.011)
    turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)



def write_letter(proposal_type, name):
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.color('black')
    turtle.write(f"Dear {name},", font=("Arial", 20, "bold"))
    turtle.penup()
    turtle.goto(-200, 170)
    turtle.pendown()
    if proposal_type == "date":
        msg = "\n\n\nWould you make my world brighter by going on a date with me?\n\n\nWith all my heart, I await your answer."
    elif proposal_type == "marriage":
        msg = "\n\n\nWill you marry me and make me the happiest person alive?\n\n\nMy love for you is eternal."
    elif proposal_type == "valentine":
        msg = "\n\n\nWill you be my Valentine?\n\n\nYou are the sweetest part of my life."
    else:
        msg = "\n\n\nYou are special to me in every way.\n\n\nWill you accept my proposal?"
    turtle.write(msg, font=("Arial", 14, "normal"))

def main():
    print("What is your proposal? (date/marriage/valentine/other)")
    proposal_type = input("Enter proposal type: ").strip().lower()
    name = input("Enter the name of your beloved: ").strip()

    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("misty rose")

    # Draw different graphics based on proposal type
    if proposal_type == "date":
        draw_flower()
    elif proposal_type == "marriage":
        draw_ring()
    elif proposal_type == "valentine":
        draw_heart()
    

    write_letter(proposal_type, name)
    turtle.done()

if __name__ == "__main__":
    main()


