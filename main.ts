let matka_location = 0
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
basic.forever(function () {
    basic.clearScreen()
    draw_matka()
})
