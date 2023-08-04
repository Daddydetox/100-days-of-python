while not is_facing_north():
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
