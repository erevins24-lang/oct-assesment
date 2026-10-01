def on_button_pressed_a():
    global guess
    guess += 1
    if guess > 9:
        guess = 1
    basic.show_number(guess)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if guess == secret:
        basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)

guess = 0
secret = 0
secret = randint(1, 9)
guess = 1
basic.show_number(guess)