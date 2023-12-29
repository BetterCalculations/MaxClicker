import client_util  # Import the auto clicker implement
import os  # Important for set title
import config_cps  # the possible cps
import cps_util  # randomised cps
os.system(f"title {client_util.client_name}  {client_util.client_version}")  # set title
print(f"{client_util.client_name} {client_util.client_version} by {client_util.client_author}")  # print clicker name
while True:
    # client loop
    if client_util.is_stop():
        # set the client in standby
        client_util.is_left = False
        client_util.is_right = False
    client_util.delay(cps_util.randomise_cps(config_cps.c))  # click delay
    client_util.left()  # wait for pressing the left hot key
    client_util.right()  # wait for pressing the right hot key

    client_util.mouse_click_event()  # start the auto clicker



