from externalpyoverlay import Overlay
from random import randint

overlay = Overlay('новый 1 - Notepad++', 0.0001)

while True:
    overlay.draw_circle(300, 300, 40, (14, 24, 184), 2)
    overlay.draw_circle(300, 300, 25, (0, 255, 0), 0)
    overlay.draw_ellipse(500, 500, 60, 20, (128, 128, 0), 8)
    overlay.draw_line(400, 380, 600, 420, (0, 107, 174), 2)
    overlay.draw_rect(200, 400, 30, 30, (199, 21, 133), 0)
    overlay.draw_rect(180, 380, 80, 120, (0, 255, 255), 1)
    overlay.draw_text('Overlay testing', ('Impact', 45), 350, 300, (randint(0, 255), randint(0, 255), randint(0, 255)), False)
    overlay.update_overlay()
