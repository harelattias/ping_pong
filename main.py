def on_button_pressed_a():
    global matka_location
    matka_location += 1
    if matka_location > 5:
        matka_location = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def draw_matka():
    if matka_location == 0:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    else:
        if matka_location == 1:
            basic.show_leds("""
                . . . . .
                                . . . . .
                                . . . . .
                                . . . . .
                                . . # # #
            """)
        else:
            if matka_location == 2:
                basic.show_leds("""
                    . . . . .
                                        . . . . .
                                        . . . . .
                                        . . . . .
                                        . # # # .
                """)
            else:
                if matka_location == 3:
                    basic.show_leds("""
                        . . . . .
                                                . . . . .
                                                . . . . .
                                                . . . . .
                                                # # # . .
                    """)
                else:
                    if matka_location == 4:
                        basic.show_leds("""
                            . . . . .
                                                        . . . . .
                                                        . . . . .
                                                        . . . . .
                                                        # # . . #
                        """)
                    else:
                        if matka_location == 5:
                            basic.show_leds("""
                                . . . . .
                                                                . . . . .
                                                                . . . . .
                                                                . . . . .
                                                                # . . # #
                            """)
                        else:
                            basic.show_number(matka_location)

def on_button_pressed_b():
    global matka_location
    matka_location += -1
    if matka_location < 1:
        matka_location = 5
input.on_button_pressed(Button.B, on_button_pressed_b)

matka_location = 0
matka_location = 0

def on_forever():
    draw_matka()
basic.forever(on_forever)
