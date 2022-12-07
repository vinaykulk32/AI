def clean(floor, goal, cost):
    for i in range(3):
        if floor == goal:
            print("attained goal state")
            print_floor(floor, cost)
            return
        if floor[i] == goal[i]:
            continue
        if floor[i] == 1:
            print("STATUS:DIRTY")
            print("room"+str(i+1))
            print_floor(floor, cost)
            floor[i] = 0
            cost += 1
            print("moving to room"+str(i+2))
        else:
            print("STATUS:CLEAN")
            print_floor(floor, cost)


def print_floor(floor, cost):
    print(floor)
    print("cost:", cost)
    print("-----------------")


# Test 1
room = [1, 1]
goal = [0, 0]
cost = 0
clean(room, goal, cost)
