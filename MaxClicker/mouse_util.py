import mouse as input
import type_util
import tick_util

block_hit_delay = 30
cps_randomised_check = 0


def click_on_fixed_pos(x, y):
    if type_util.is_int(x) and type_util.is_int(y):
        input.move(x, y)  # set mouse pos to a fixed mouse pos


def get_mouse_pos():
    return input.get_position()     # get mouse pos as list


def get_x():
    return get_mouse_pos()[0]   # get mouse pos x


def get_y():
    return get_mouse_pos()[1]   # get mouse pos y


def left_click():
    input.click(input.LEFT)     # click left


def right_click():
    input.click(input.RIGHT)    # click right


def right_double_click():
    input.double_click(input.RIGHT)     # double click right


def left_double_click():
    input.double_click(input.LEFT)      # double click right


def press_right():
    input.press(input.RIGHT)    # press right mouse button I need this for block hit function


def press_left():
    input.press(input.LEFT)     # press left mouse button


def release_left():
    input.release(input.LEFT)       # release left mouse button


def release_right():
    input.release(input.RIGHT)      # release right mouse button


def block_hit():
    global block_hit_delay
    if block_hit_delay == 0:
        press_right()
        press_left()
        release_left()
        # is delay 0 then block hit ^
        release_right()
        block_hit_delay = tick_util.get_random_tick()   # set new random tick

