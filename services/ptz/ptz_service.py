

def move(x: float, y: float, action: str):
    if action == 'Start':
        if x > 0:
            move_right()
        if x < 0:
            move_left()
        if y > 0:
            move_up()
        if y < 0:
            move_down()


def move_left():
    print("Moving left")

def move_right():
    print("Moving right")

def move_up():
    print("Moving up")

def move_down():
    print("Moving down")