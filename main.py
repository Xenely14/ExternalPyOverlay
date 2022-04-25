from externalpyoverlay import Overlay

overlay = Overlay('test.txt - Блокнот', 0.0001)

while True:
    overlay.draw_circle(300, 300, 40, (14, 24, 184), (2))
    overlay.update_overlay()