matka_location = 0


def on_button_pressed_a():
    global matka_location
    matka_location += -1
    if matka_location < 0:
        matka_location = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def calculate_racket_location(loc: number):
    if loc > 4:
        loc = 0
    elif loc < 0:
        loc = 4
    return loc


def draw_matka():
    led.plot(0 + matka_location, 4)
    led.plot(1 + matka_location, 4)
    led.plot(2 + matka_location, 4)

def on_button_pressed_b():
    global matka_location
    matka_location = calculate_racket_location(1 + matka_location)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.clear_screen()
    draw_matka()
basic.forever(on_forever)
