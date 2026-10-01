input.onButtonPressed(Button.A, function () {
    guess += 1
    if (guess > 9) {
        guess = 1
    }
    basic.showNumber(guess)
})
input.onButtonPressed(Button.B, function () {
    if (guess == secret) {
        basic.showIcon(IconNames.Happy)
    }
})
let guess = 0
let secret = 0
secret = randint(1, 9)
guess = 1
basic.showNumber(guess)
