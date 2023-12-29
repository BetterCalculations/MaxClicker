def write(filename, text):
    file = open(filename, "w")      # open a file
    file.write(text)                # write a file
    file.close()                    # close the file
