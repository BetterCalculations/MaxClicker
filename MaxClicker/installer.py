import os
# If you work in anaconda can you use this installer for install the required modules
modules = ["keyboard", "mouse"]


def install():
    for elm in modules:
        os.system(f"pip install {elm} ")


install()
