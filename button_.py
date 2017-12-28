from graphics import *

W, H = 400,400


class Choice_Panel:
    def __init__(self, window, n):
        buttons = []
        msgs = []
        j = 0
        f = 1./n/2.
        k = 1./n
        count = 0
        shapes = ["circle","rect","triangle","quad","key\npainter","color","randomize\nkey\npainter\nsettings","quit"]
        for x in range(1, n + 1):
            c1 = Point( j * W, 0 * H)
            c2 = Point( k * W, 0 * H )
            c3 = Point( k * W, 1./n * H )
            c4 = Point( j * W, 1./n * H)
            b = Button(window, c1, c2, c3, c4)
            msg = Text(Point( f * W, 1./n/2 * H), shapes[count])
            msg.setSize(8)
            if count == 4 or count == 6:
                msg.setSize(7)
            msg.draw(window)
            buttons.append(b)
            msgs.append(msg)
            j += 1./n
            k += 1./n
            f += 1./n
            count += 1
        self.buttons = buttons
        self.msgs = msgs

    def clicked_button(self, point):
        i = 1
        return_button_index = -1
        return_button = -1
        for button in self.buttons:
            if not button.clicked(point) and i != 6:
                button.polygon.setFill("white")
            elif button.clicked(point):
                button.polygon.setFill("blue")
                return_button = button
                return_button_index = i
            i += 1
        return [return_button_index, return_button]

    def __del__(self):
        for button in self.buttons:
            button.polygon.setFill("white")
            button.polygon.undraw()
        for msg in self.msgs:
            msg.undraw()

class Button:
    
    def __init__(self, window, c1, c2, c3, c4):
        polygon = Polygon(c1, c2, c3, c4)
        self.polygon = polygon
        polygon.setFill("white")
        polygon.draw(window)
        self.c1, self.c2, self.c3, self.c4 = c1, c2, c3, c4
    def clicked(self, point):
        px, py = point.getX(), point.getY()
        return px > self.c1.getX() and px < self.c2.getX() and py > self.c1.getY() and  py < self.c4.getY()
