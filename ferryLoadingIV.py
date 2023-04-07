test_cases = int(input())


for _ in range(test_cases):
    ferry_length, num_cars = [int(x) for x in input().split()]
    ferry_length *= 100 # in centimeters
    left_cars = [] # front of array is the front of the line
    right_cars = []

    for _ in range(num_cars):
        car_len, direction = input().split()
        car_len = int(car_len)

        if direction == "left":
            left_cars.append(car_len)
        elif direction == "right":
            right_cars.append(car_len)
     
    print("left:", left_cars, "right:", right_cars)

    times_crossed = 0
    loaded_cars = 0
    on_left_side = True
    while len(left_cars)>0 or len(right_cars)>0:
        if on_left_side and len(left_cars)>0:
            while len(left_cars)>0 and (loaded_cars+left_cars[0]) <= ferry_length:
                loaded_cars += left_cars.pop(0)
            times_crossed += 1
            loaded_cars = 0
            on_left_side = not on_left_side
        elif not on_left_side and len(right_cars)>0:
            while len(right_cars)>0 and (loaded_cars+right_cars[0]) <= ferry_length:
                loaded_cars += right_cars.pop(0)
            times_crossed += 1
            loaded_cars = 0
            on_left_side = not on_left_side
        else:
            on_left_side = not on_left_side
            times_crossed += 1

        print("left:", left_cars, "right:", right_cars)

    print("--", times_crossed, "--")


