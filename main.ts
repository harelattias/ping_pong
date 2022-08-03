input.onButtonPressed(Button.A, function () {
    matka_location += 1
    if (matka_location > 5) {
        matka_location = 1
    }
})
function draw_matka () {
    if (matka_location == 0) {
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    } else {
        if (matka_location == 1) {
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # # #
                `)
        } else {
            if (matka_location == 2) {
                basic.showLeds(`
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . # # # .
                    `)
            } else {
                if (matka_location == 3) {
                    basic.showLeds(`
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        # # # . .
                        `)
                } else {
                    if (matka_location == 4) {
                        basic.showLeds(`
                            . . . . .
                            . . . . .
                            . . . . .
                            . . . . .
                            # # . . #
                            `)
                    } else {
                        if (matka_location == 5) {
                            basic.showLeds(`
                                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                # . . # #
                                `)
                        } else {
                            basic.showNumber(matka_location)
                        }
                    }
                }
            }
        }
    }
}
input.onButtonPressed(Button.B, function () {
    matka_location += -1
    if (matka_location < 1) {
        matka_location = 5
    }
})
let matka_location = 0
matka_location = 0
basic.forever(function () {
    draw_matka()
})
