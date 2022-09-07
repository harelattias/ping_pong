function draw_ball () {
    led.plot(ball_loc_x, ball_loc_y)
}
input.onButtonPressed(Button.A, function () {
    matka_location = calculate_racket_location(-1 + matka_location)
})
function calculate_racket_location (loc: number) {
    return (loc + 5) % 5
}
function draw_matka () {
    led.plot(calculate_racket_location(0 + matka_location), 4)
    led.plot(calculate_racket_location(1 + matka_location), 4)
    led.plot(calculate_racket_location(2 + matka_location), 4)
}
input.onButtonPressed(Button.B, function () {
    matka_location = calculate_racket_location(1 + matka_location)
})
function calc_ball_loc () {
    ball_loc_x = ball_velocity_x + ball_loc_x
    ball_loc_y = ball_velocity_y + ball_loc_y
    if (3 == ball_loc_y) {
        if (ball_loc_x == 0 + matka_location) {
            ball_velocity_x = -1
            ball_velocity_y = -1
        } else {
            if (ball_loc_x == 1 + matka_location) {
                ball_velocity_x = 0
                ball_velocity_y = -1
            } else {
                if (ball_loc_x == 2 + matka_location) {
                    ball_velocity_x = 1
                    ball_velocity_y = -1
                } else {
                    the_end_game = 8
                }
            }
        }
    }
    if (0 == ball_loc_y) {
        ball_velocity_y = 1
    }
    if (4 == ball_loc_x) {
        ball_velocity_x = -1
    }
    if (0 == ball_loc_x) {
        ball_velocity_x = 1
    }
}
let the_end_game = 0
let matka_location = 0
let ball_velocity_y = 0
let ball_velocity_x = 0
let ball_loc_y = 0
let ball_loc_x = 0
ball_loc_x = 2
ball_loc_y = 1
ball_velocity_x = 1
ball_velocity_y = 1
basic.forever(function () {
    basic.clearScreen()
    draw_matka()
    draw_ball()
    calc_ball_loc()
    if (8 == the_end_game) {
        basic.showIcon(IconNames.Sad)
        music.playMelody("C5 C D E F G A B ", 120)
    }
    basic.pause(1000)
})
