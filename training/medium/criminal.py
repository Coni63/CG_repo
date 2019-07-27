# (1) INPUT
height = int(input())
width  = int(input())

# (2) MY VARIABLES
people    = []
obstacles = []
you       = []
n_are_watching_you = 0

# (2.1) LOAD MY VARIABLES
for y in range(height):
    row = input()
    for x in range(len(row)):
        if row[x] == ' ': continue

        if row[x] in ['^','>','v','<']:
            person = [x,y,['^','>','v','<'].index(row[x])]
            people.append(person)
            obstacles.append(person[0:2])
        elif row[x] == 'Y':
            you = [x,y]
        else:
            obstacle = [x,y]
            obstacles.append(obstacle)

# (3) FOREACH PEOPLE
for person in people:
    # (3.1) FOREACH VARIABLES
    person_x, person_y, person_direction = person
    field_of_vision           = []
    field_of_vision_start     = []
    field_of_vision_increment = 3
    hidden = []
    border_up_distance    = height-(height-person_y)
    border_right_distance = width-person_x
    border_down_distance  = height-person_y
    border_left_distance  = width-(width-person_x)

    # (3.2) IF PERSON LOOKS UP
    if person_direction == 0:
        field_of_vision_start_x = person_x
        field_of_vision_start_y = person_y
        for field_of_vision_y in range(border_up_distance):
            field_of_vision_start_x -= 1
            field_of_vision_start_y -= 1
            for field_of_vision_x in range(field_of_vision_increment):
                field_of_vision.append([field_of_vision_start_x+field_of_vision_x, field_of_vision_start_y])
            field_of_vision_increment+=2

        for obstacle in obstacles:
            if not obstacle in field_of_vision: continue
            obstacle_x, obstacle_y = obstacle
            hidden_start_x   = obstacle_x
            hidden_start_y   = obstacle_y
            hidden_increment = 2
            # (3.2.0.1) IF obstacle is to the front of the person
            if obstacle_x == person_x:
                hidden_start_y -= 1
                for hidden_y in range(border_up_distance):
                    hidden.append([hidden_start_x, hidden_start_y-hidden_y])

            # (3.2.0.2) IF obstacle is to the right
            elif obstacle_x > person_x:
                for hidden_y in range(border_up_distance):
                    hidden_start_y -= 1
                    for hidden_x in range(hidden_increment):
                        hidden.append([hidden_start_x+hidden_x, hidden_start_y-hidden_y])
                hidden_increment += 1

            # (3.2.0.3) IF obstacle is to the left
            elif obstacle_x < person_x:
                for hidden_y in range(border_up_distance):
                    hidden_start_y -= 1
                    for hidden_x in range(hidden_increment):
                        hidden.append([hidden_start_x-hidden_x, hidden_start_y-hidden_y])
                hidden_increment += 1

    # (3.3) IF PERSON LOOKS RIGHT
    elif person_direction == 1:
        field_of_vision_start_x = person_x
        field_of_vision_start_y = person_y
        for field_of_vision_x in range(border_right_distance):
            field_of_vision_start_x += 1
            field_of_vision_start_y -= 1
            for field_of_vision_y in range(field_of_vision_increment):
                field_of_vision.append([field_of_vision_start_x, field_of_vision_start_y+field_of_vision_y])
            field_of_vision_increment+=2

        for obstacle in obstacles:
            if not obstacle in field_of_vision: continue
            obstacle_x, obstacle_y = obstacle
            hidden_start_x   = obstacle_x
            hidden_start_y   = obstacle_y
            hidden_increment = 2

            # (3.3.0.1) IF obstacle is to the front of the person
            if obstacle_y == person_y:
                for hidden_x in range(border_right_distance):
                    hidden.append([hidden_start_x+hidden_x, hidden_start_y])

            # (3.3.0.2) IF obstacle is down
            elif obstacle_y > person_y:
                hidden_start_x += 1
                for hidden_x in range(border_right_distance):
                    for hidden_y in range(hidden_increment):
                        hidden.append([hidden_start_x+hidden_x, hidden_start_y+hidden_y])
                    hidden_increment += 1

            # (3.3.0.2) IF obstacle is up
            elif obstacle_y < person_y:
                hidden_start_x += 1
                for hidden_x in range(border_right_distance):
                    for hidden_y in range(hidden_increment):
                        hidden.append([hidden_start_x+hidden_x, hidden_start_y-hidden_y])
                    hidden_increment += 1

    # (3.4) IF PERSON LOOKS DOWN
    elif person_direction == 2:
        field_of_vision_start_x = person_x
        field_of_vision_start_y = person_y
        for field_of_vision_y in range(border_down_distance):
            field_of_vision_start_x -= 1
            field_of_vision_start_y += 1
            for field_of_vision_x in range(field_of_vision_increment):
                field_of_vision.append([field_of_vision_start_x+field_of_vision_x, field_of_vision_start_y])
            field_of_vision_increment+=2

        for obstacle in obstacles:
            if not obstacle in field_of_vision: continue
            obstacle_x, obstacle_y = obstacle
            hidden_start_x   = obstacle_x
            hidden_start_y   = obstacle_y
            hidden_increment = 2

            # (3.4.0.1) IF obstacle is to the front
            if obstacle_x == person_x:
                hidden_start_y += 1
                for hidden_y in range(border_down_distance):
                    hidden.append([hidden_start_x, hidden_start_y+hidden_y])

            # (3.4.0.2) IF obstacle is to the right
            elif obstacle_x > person_x:
                for hidden_y in range(border_down_distance):
                    hidden_start_y += 1
                    for hidden_x in range(hidden_increment):
                        hidden.append([hidden_start_x+hidden_x, hidden_start_y])
                hidden_increment += 1

            # (3.4.0.3) IF obstacle is to the left
            elif obstacle_x < person_x:
                for hidden_y in range(border_down_distance):
                    hidden_start_y += 1
                    for hidden_x in range(hidden_increment):
                        hidden.append([hidden_start_x+hidden_x, hidden_start_y])
                hidden_increment += 1

    # (3.5) IF PERSON LOOKS LEFT
    elif person_direction == 3:
        field_of_vision_start_x = person_x
        field_of_vision_start_y = person_y
        for field_of_vision_x in range(border_left_distance):
            field_of_vision_start_x -= 1
            field_of_vision_start_y -= 1
            for field_of_vision_y in range(field_of_vision_increment):
                field_of_vision.append([field_of_vision_start_x, field_of_vision_start_y+field_of_vision_y])
            field_of_vision_increment+=2
        for obstacle in obstacles:
            if not obstacle in field_of_vision: continue
            obstacle_x, obstacle_y = obstacle
            hidden_start_x   = obstacle_x
            hidden_start_y   = obstacle_y
            hidden_increment = 2

            # (3.5.0.1) IF obstacle is to the front of the person
            if obstacle_y == person_y:
                for hidden_x in range(border_left_distance):
                    hidden.append([hidden_start_x-hidden_x, hidden_start_y])

            # (3.5.0.2) IF obstacle is down
            elif obstacle_y > person_y:
                hidden_start_x -= 1
                for hidden_x in range(border_left_distance):
                    for hidden_y in range(hidden_increment):
                        hidden.append([hidden_start_x-hidden_x, hidden_start_y+hidden_y])
                    hidden_increment += 1

            # (3.5.0.2) IF obstacle is up
            elif obstacle_y < person_y:
                hidden_start_x -= 1
                for hidden_x in range(border_left_distance):
                    for hidden_y in range(hidden_increment):
                        hidden.append([hidden_start_x-hidden_x, hidden_start_y-hidden_y])
                    hidden_increment += 1

    # (3.6) DETECT if you are in field of vision of a person
    if you in field_of_vision and not you in hidden:
#        print(person)
        n_are_watching_you+=1


# (4) OUTPUT

# (4.1) HELP
"""
print('+------------------HELP-------------------')
print('| people:            ', people             )
print('| obstacles:         ', obstacles          )
print('| you:               ', you                )
print('| n_are_watching_you:', n_are_watching_you )
print('+-----------------------------------------')
"""

# (4.2) FINAL OUTPUT
print(n_are_watching_you)

