# solvedem

from button_ import *
from helper import *

W, H = 400, 400
win = GraphWin("Doodle", W, H)
win.setCoords(0, 0, W, H)
choice_panel = Choice_Panel(win, 8)
user_choice, color_count, randomize_, QUIT = -1, 1, 0, 8
colors = ["white","yellow","green","cyan","purple","pink","blue"]
color = colors[0]

while user_choice != QUIT:
    
    panel = choice_panel.clicked_button(win.getMouse())
    user_choice, button = panel[0], panel[1]
    
    if user_choice == 1:
        draw_circle(color, button, win)

    if user_choice == 2:
        draw_rect(color, button, win)

    if user_choice == 3:
        draw_triangle(color, button, win)
        
    if user_choice == 4:
        draw_quad(color, button, win)

    if user_choice == 5:
        key(color, button, randomize_, win)

    if user_choice == 6:
        if color_count >= len(colors):
            color_count = 0
        color = colors[color_count]
        button.polygon.setFill(color)
        color_count += 1
        
    if user_choice == 7:
        randomize_ = choice([1,2,3,4])

win.close()
