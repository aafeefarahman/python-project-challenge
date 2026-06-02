from time import *
import random as r


def mistake(paratest, usertest):
    error = 0

    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error += 1
        except:
            error += 1

    return error


def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)

    if time_R == 0:
        return 0

    speed = len(userinput) / time_R
    return round(speed)


test = [
    "lorem ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
    "ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat",
    "duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur",
    "excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum"
]

while True:

    test1 = r.choice(test)

    print("\n********** TYPING SPEED TEST **********\n")
    print(test1)
    print()

    time_1 = time()

    testinput = input("Enter : ")

    time_2 = time()

    print("Speed :", speed_time(time_1, time_2, testinput), "w/sec")
    print("Error :", mistake(test1, testinput))

    ck = input("\nReady to test : yes / no : ").lower()

    if ck == "yes":
        continue

    elif ck == "no":
        print("Thank You")
        break

    else:
        print("Wrong Input")
        break