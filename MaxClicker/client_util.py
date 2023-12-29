import hotkeys      # import the hotkeys
from var_util import *     # True = true, False = false
import time                 # import the delay function
import config_cps as cp     # import the cps config for randomise check
import cps_util as cu       # import the cps util for generate randomised cps
import cps as clicks        # import the cps creator
import mouse_util           # import the mouse util for some function for example click on fixed mouse position
import pos_config           # import your position config
import keyboard_util        # import the keyboard util for is key down

client_version = "1.0"  # client version
client_author = "LiriumKonsument"   # client Author
client_name = "Maxi Clicker "       # Client Name
past_cps = 0                        # past cps check var
last_cps = 0                        # last cps check var
current_cps = 0                     # current cps in the delay function
is_block = false                    # true = block hit in minecraft is active false = block hit in minecraft is deactive
is_left = false                     # check var for clicking left
is_right = false                    # check var for clicking right
is_position_click = false           # if you want click on a fixed mouse position then you can set to true
double_click = false                # if you want the client should clicking with double clicks you can set it true


def delay(cps):
    global current_cps, last_cps, past_cps
    current_cps = cps  # set the current cps
    if mouse_util.cps_randomised_check == 0:
        last_cps = cps  # set the last cps

    if mouse_util.cps_randomised_check == 1:
        if last_cps == current_cps:
            past_cps = last_cps  # set the past cps
            cps = cu.randomise_cps(clicks.create(cp.c[0], cp.c[1]))  # set a new cps value
            last_cps = cps  # set the last cps

    if mouse_util.cps_randomised_check == 2:
        if past_cps == current_cps:
            cps = cu.randomise_cps(clicks.create(cp.c[0], cp.c[1]))  # set a new cps value
            mouse_util.cps_randomised_check = -1  # set the check to - 1

    time.sleep(1/cps)   #  set the clicking delay

    mouse_util.cps_randomised_check += 1  # logic for last and past randomise cps


def mouse_click_event():

    if is_position_click is true:
        mouse_util.click_on_fixed_pos(pos_config.x, pos_config.y)  # click on a fixed mouse pos
        if mouse_util.get_x() == pos_config.x and mouse_util.get_y() == pos_config.y:
            if is_right:
                mouse_util.right_click()
            if is_left:
                mouse_util.left_click()

    if double_click is false and is_position_click is false:
        if is_right:
            mouse_util.right_click()       # Right Auto click
        if is_left:
            if is_block:
                mouse_util.block_hit()  # auto block auto click
                mouse_util.block_hit_delay -= 1  # -= 1 auto block delay

            mouse_util.left_click()  # Right Auto click
    if double_click is true and is_position_click is false:
        if is_right:
            mouse_util.right_double_click()  # auto double clicking right
        if is_left:
            mouse_util.left_double_click()  # auto double clicking left


def is_stop():
    if keyboard_util.is_key_down(hotkeys.STOP):
        return true     # set the client in standby see in the client file
    else:
        return false    # the client is in action


def left():
    global is_right, is_left
    if keyboard_util.is_key_down(hotkeys.LEFT) and is_left is true:
        is_left = false     # toggle off left auto clicker
    elif keyboard_util.is_key_down(hotkeys.LEFT) and is_left is false:
        if is_right is true and is_left is false:
            # is right clicker on then deactive right auto clicker
            is_right = false    # toggle off right auto clicker
            is_left = true  # toggle on left auto clicker
        else:
            is_left = true  # toggle on left auto clicker


def right():
    global is_left, is_right
    if keyboard_util.is_key_down(hotkeys.RIGHT) and is_right is true:
        is_right = false    # toggle off right auto clicker
    elif keyboard_util.is_key_down(hotkeys.RIGHT) and is_right is false:
        if is_left:
            is_right = true     # toggle on right auto clicker
            is_left = false     # toggle off left auto clicker
        else:
            is_right = true     # toggle on right auto clicker

