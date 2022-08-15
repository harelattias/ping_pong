matka_location = 0

def on_button_pressed_a():
    global matka_location
    matka_location = calculate_racket_location(-1 + matka_location)
input.on_button_pressed(Button.A, on_button_pressed_a)

def calculate_racket_location(loc: number):
    return (loc + 5) % 5
    
def draw_matka():
    led.plot(calculate_racket_location(0 + matka_location), 4)
    led.plot(calculate_racket_location(1 + matka_location), 4)
    led.plot(calculate_racket_location(2 + matka_location), 4)

def on_button_pressed_b():
    global matka_location
    matka_location = calculate_racket_location(1 + matka_location)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.clear_screen()
    draw_matka()
basic.forever(on_forever)
