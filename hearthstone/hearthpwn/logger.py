log = ""


def print_log():
    print(log)


def append_log(string):
    global log
    log += "\n" + string
    print(string)
