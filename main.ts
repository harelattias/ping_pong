let matka_location = 0
let loc = 0
input.onButtonPressed(Button.A, function () {
    matka_location = calculate_racket_location(-1 + matka_location)
})
function calculate_racket_location (loc: number) {
    if (loc > 4) {
        loc = 0
    } else if (loc < 0) {
        loc = 4
    }
    return loc
}
function draw_matka () {
    led.plot(0 + matka_location, 4)
    led.plot(1 + matka_location, 4)
    led.plot(2 + matka_location, 4)
}
input.onButtonPressed(Button.B, function () {
    matka_location = calculate_racket_location(1 + matka_location)
})
basic.forever(function () {
    basic.clearScreen()
    draw_matka()
})
