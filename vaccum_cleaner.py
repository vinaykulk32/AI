def clean(floor, goal):
    for i in range(3):
        if floor == goal:
            print("attained goal state")
            print_floor(floor)
            return
        if floor[i] == goal[i]:
            continue
        if floor[i] == 1:
            print("STATUS:DIRTY")
            print_floor(floor)
            floor[i] = 0
        else:
            print("STATUS:CLEAN")
            print_floor(floor)


def print_floor(floor):
    print(floor)
    print("-----------------")


# Test 1
room = [0, 0]
goal = [0, 0]
clean(room, goal)
