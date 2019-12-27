#this is made by progress osemudiamen emuan i din'tt use any libraries to make this library i am making it myself
# without the help of internet but only of the book i wrote with notes from solo learn python book
import os
import subprocess
import sys

def CommandLine():
    class CoordinatesManager:
        def __init__(self, coordinates_x, coordinates_y):
            self.coordinates_x = coordinates_x
            self.coordinates_y = coordinates_y
        def reset(self, coordinates_mix):
            self.coordinates_mix = list(str(self.coordinates_x) + ", " + str(self.coordinates_y))
            decision_reset = input("The current coordinates are: " + str(self.coordinates_x) + ", " + str(self.coordinates_y) + " Are you sure you want to reset:")
            if decision_reset == "yes":
                self.coordinates_y = 0
                self.coordinates_x = 0
            elif decision_reset == "no":
                print("The coordinates are the same as before: " + str(self.coordinates_y) + " " + str(self.coordinates_x))
            else:
                print("The coordinates were not changed but the input reply was incorrect")

        def increase(self, coordinates_x, coordinates_y, value):
            coordinates_x += int(value)
            coordinates_y += int(value)
        def decrease(self, coordinates_x, coordinates_y, value):
            coordinates_y -= int(value)
            coordinates_x -= int(value)
        def join(self, coordinates_x, coordinates_y):
            coordinates_mix = str(coordinates_y) + " " + str(coordinates_x)
            return coordinates_mix
        def separate(self, coordinates_mix):
            coordinates_list = coordinates_mix.split()
            coordinates_y = coordinates_list[0]
            coordinates_x = coordinates_list[2]
            return coordinates_y, coordinates_x
    coordinates_Manager = CoordinatesManager(0, 0)
    print("Current coordinates are y: " + str(coordinates_Manager.coordinates_y) + " x:" + str(coordinates_Manager.coordinates_x))
    run = True
    while True:
        commandline = input("Now use the movement keys to change coordinates tyoe a command using the keys "
                            "for more info use help in the main screen to enter mainscreen type quit if not use "
                            "the movement keys: ")
        for letter in commandline:
            if letter == "a":
                coordinates_Manager.coordinates_x -= 20
            elif letter == "d":
                coordinates_Manager.coordinates_x += 20
            elif letter == "w":
                coordinates_Manager.coordinates_y += 20
            elif letter == "s":
                coordinates_Manager.coordinates_y -= 20
            else:
                print("unknown Key")
        else:
            print("This are the coordinates " + str(coordinates_Manager.coordinates_y) + ", " + str(coordinates_Manager.coordinates_x))
            continue_decision = input("Do you want to write another command line: ")
            if continue_decision == "yes" or continue_decision == "YES":
                continue
            elif continue_decision == "no" or continue_decision == "NO":
                print("\n\n")
                subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
            elif continue_decision == "quit":
                print("\n\n")
                subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
            else:
                print("unknown Key")
def help_function():
    print("Hi this is the help guide of this app.\n"
          "In anywhere inside this app where you are required to input anything you can type quit to come back to main screen\n"
          "It is reccomended to use small letters in every input of the app\n"
          "for the movement keys to to reduce delay in anilizing each key and adding the following data to x and y positions\n"
          "Movement Keys:\n"
          "a    changes -20 to the x coordinates\n"
          "d    changes +20 to the x coordinates\n"
          "w    changes +20 to the y coordinates\n"
          "s    changes -20 to the y coordinates\n"
          "Note!\n + in the y coordinates in going up - in going down while in the x coordinates + is right and - is left"
          "Command Line Example:\n adwdsdawwwsd"
          "\n The coordinates are 60 y and 60 x\n "
          "Note!\n"
          "The first number is y and the second is x")
    quit_action = input("Write exit to go back to main screen: ")
    if quit_action == "quit":
        print("\n\n")
        subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
    else:
        print("Unknown Key")
def startUp():
    mainscreen_action = input()
    if mainscreen_action == "start":
        CommandLine()
    elif mainscreen_action == "--help":
        help_function()
    else:
        print("unknown function")
print("Helo welcome to this library called ProgressCoordinates\n"
      "You can start by writing start (to start The coordinates functions) or --help to check the guide")
startUp()


