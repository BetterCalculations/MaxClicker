import keyboard as input


def jump():
    input.release("space")  # is not working I don't know why


def is_key_down(key):
    if type(key) != str:
        return  # if key not a string
    if input.is_pressed(key):
        return True     # is key down then return True
    else:
        return False    # else return False
