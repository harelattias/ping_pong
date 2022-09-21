def draw_ball():
    led.plot(ball_loc_x, ball_loc_y)

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

def calc_ball_loc():
    global ball_velocity_x, ball_velocity_y, the_end_game, num_of_fails, ball_loc_x, ball_loc_y
    if 3 == ball_loc_y:
        if ball_loc_x == 0 + matka_location:
            ball_velocity_x = -1
            ball_velocity_y = -1
        elif ball_loc_x == 1 + matka_location:
            ball_velocity_x = 0
            ball_velocity_y = -1
        elif ball_loc_x == 2 + matka_location:
            ball_velocity_x = 1
            ball_velocity_y = -1
        else:
            the_end_game = 1
            num_of_fails += 1
    if 0 == ball_loc_y:
        ball_velocity_y = 1
    if 4 == ball_loc_x:
        ball_velocity_x = -1
    if 0 == ball_loc_x:
        ball_velocity_x = 1
    ball_loc_x = ball_velocity_x + ball_loc_x
    ball_loc_y = ball_velocity_y + ball_loc_y
def reset_game():
    global ball_loc_x, ball_loc_y, ball_velocity_x, ball_velocity_y, the_end_game
    ball_loc_x = 1
    ball_loc_y = 1
    ball_velocity_x = 1
    ball_velocity_y = 1
    the_end_game = 0
the_end_game = 0
ball_velocity_y = 0
ball_velocity_x = 0
matka_location = 0
ball_loc_y = 0
ball_loc_x = 0
reset_game()
num_of_fails = 0

def on_forever():
    if num_of_fails == 3:
        basic.show_icon(IconNames.SAD)
        music.play_melody("C5 C D E F G A B ", 500)
        basic.pause(2000)
    else:
        if 1 == the_end_game:
            reset_game()
        else:
            basic.clear_screen()
            draw_matka()
            draw_ball()
            calc_ball_loc()
            basic.pause(1000)
basic.forever(on_forever)
