from microbit import *
import radio

def shift_letter(letter: str, amount: str) -> str:
    letter_num = ord(letter) - ord('A')
    shifted_letter_num = (letter_num + amount) % 26
    return chr(ord('A') + shifted_letter_num)

def shift_message(message: str, amount: str) -> str:
    shifted_message = map(lambda l: shift_letter(l, shift_amount), message)
    return ''.join(shifted_message)

def shift_message_simple(message: str, amount: str) -> str:
    shifted_message = ""
    for l in message:
        shifted_message += shift_letter(l, amount)
    return shifted_message

radio.on()
radio.config(channel=7) # Make sure you are using the same channel number as the sender!
                        # Remember, knowing the channel number isn't cheating.

message = ""
shift_amount = 0

while True:
    button_a_pressed = button_a.was_pressed()
    button_b_pressed = button_b.was_pressed()

    if button_a_pressed:
        shift_amount -= 1

    if button_b_pressed:
        shift_amount += 1

    letter = radio.receive()

    if letter:
        display.show(letter)
        message += letter
        sleep(500)

    letter = None

    display.scroll(shift_message(message, shift_amount))