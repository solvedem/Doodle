from graphics import *
from random import choice

W, H = 400, 400

def distance_(p1, p2):
    x1, x2 = p1.getX(), p2.getX()
    y1, y2 = p1.getY(), p2.getY()
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5

def draw_circle(color, button, win):
    msg = Text(Point(W - 20, H - 20), "2")
    msg.draw(win)
    center = win.getMouse()
    msg.setText("1")
    pre_circle = Circle(center,2)
    pre_circle.draw(win)
    p2 = win.getMouse()
    msg.undraw()
    circle = Circle(center, distance_(center, p2))
    pre_circle.undraw()
    circle.setFill(color)
    button.polygon.setFill("white")
    circle.draw(win)

def draw_rect(color, button, win):
    msg = Text(Point(W - 20, H - 20), "2")
    msg.draw(win)
    p1 = win.getMouse()
    msg.setText("1")
    p2 = win.getMouse()
    msg.undraw()
    x_length = abs(p2.getX() - p1.getX())
    y_length = abs(p2.getY() - p1.getY())
    if p2.getX() > p1.getX():
        p3 = Point(x_length + p1.getX(), p1.getY())
        p4 = Point(p1.getX(), y_length + p1.getY())
        if p2.getY() < p1.getY():
            p4 = Point(x_length + p1.getX(), p1.getY())
            p3 = Point(p1.getX(), p1.getY() - y_length)
    else:
        p3 = Point(p1.getX() - x_length, p1.getY())
        p4 = Point(p1.getX(), p1.getY() - y_length)
        if p2.getY() > p1.getY():
            p3 = Point(p1.getX(), p1.getY() + y_length)
            p4 = Point(p1.getX() - x_length, p1.getY())
    poly = Polygon(p1,p3,p2,p4)


    poly.draw(win)
    poly.setFill(color)
    button.polygon.setFill("white")


def draw_triangle(color, button, win):
    msg = Text(Point(W - 20, H - 20), "3")
    msg.draw(win)
    
    p1 = win.getMouse()
    msg.setText("2")
    pre_circle = Circle(p1,2)
    pre_circle.draw(win)

    p2 = win.getMouse()
    msg.setText("1")
    line = Line(p1,p2)
    line.draw(win)
    pre_circle.undraw()

    p3 = win.getMouse()
    msg.undraw()
    poly = Polygon(p1,p2,p3)
    line.undraw()
    poly.setFill(color)
    poly.draw(win)

    button.polygon.setFill("white")

def draw_quad(color, button, win):
    msg = Text(Point(W - 20, H - 20), "4")
    msg.draw(win)
    p1 = win.getMouse()
    msg.setText("3")
    p2 = win.getMouse()
    msg.setText("2")
    p3 = win.getMouse()
    msg.setText("1")
    p4 = win.getMouse()
    msg.undraw()
    poly = Polygon(p1,p2,p3,p4)
    poly.setFill(color)
    poly.draw(win)
    button.polygon.setFill("white")

def get_input(input_box, win):
    win.getMouse()
    n = input_box.getText()
    try:
        n = int(n)
    except:
        return get_input(input_box)
    input_box.undraw()
    return n
    
def key(color, button, randomize_, win):
    msg = Text(Point(W - 60, H - 20), "2")
    msg.draw(win)
    center = win.getMouse()
    msg.setText("1")
    pre_circle = Circle(center,2)
    pre_circle.draw(win)
    p2 = win.getMouse()
    msg.setText("")
    r = distance_(center, p2)
    r_initial, r_copy = r, r
    circle = Circle(center, r)
    pre_circle.undraw()
    circle.setFill(color)
    msg.setText("Enter n: ")
    input_ = Entry(Point(W - 60, H - 40),10)
    input_.draw(win)
    n = get_input(input_, win)
    msg.setText(str(n))
    count_down = n
    for i in range(n):
        key = win.getKey()
        if key == "Left":
            center = Point((center.getX() - 10), center.getY())
        if key == "Right":
            center = Point((center.getX() + 10), center.getY())
        if key == "Up":
            center = Point((center.getX()), center.getY() + 10)
        if key == "Down":
            center = Point((center.getX()), center.getY() - 10)
        if randomize_ == 2:
            r -= 3
            if r < 1:
                r = r_initial
        if randomize_ == 3:
            r += 3
        if randomize_ == 4:
            if i % 2 == 0:
                r *= 2
            else:
                r /= 4.
            if i % 10 == 0:
                r = r_initial
        circle = Circle(center, r)
        circle.setFill(color)
        circle.draw(win)
        if randomize_ == 1:
            r_copy += 2
            circle2 = Circle(center, r_copy)
            rc = choice(['peachpuff','cyan','pink','white'])
            circle2.setFill(rc)
            circle2.draw(win)
            if r_copy > r_initial + 20:
                r_copy = r_initial
        count_down -= 1
        msg.setText(str(count_down))
    msg.undraw()
    button.polygon.setFill("white")
