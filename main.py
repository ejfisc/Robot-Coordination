#! python3
# main.py - main driver program for the robot coordination system
import os, time, map_data
import matplotlib.pyplot as plt

# users dictionary - username: password
users = {'Ethan': 'Fischer', 'user': 'pass'}

# create the map
rows, cols = (15, 15)
fig, ax = plt.subplots(figsize=(8,8))
ax.set_title('Robot-Coordination Map')
ax.set_xlim(0, cols)
ax.set_ylim(0, rows)
robot_map = map_data.Robot_Map(rows, cols, fig, ax) 
plt.connect('button_press_event', robot_map.on_click)

# prompts the user to login and welcomes them after they have provided correct credentials
def login():
    os.system('cls||clear')
    print('LOG IN\n')
    while True:
        # prompt user for credentials
        username = input('Enter username:   ')
        password = input('Enter password:   ')

        # check if credentials are valid
        if username not in users.keys() or users.get(username) != password:
            print('Username or password is incorrect, try again.')
            continue
        elif users.get(username) == password:
            # go to welcome screen
            os.system('cls||clear')
            print(f'Welcome, {username}')
            print('Going to home screen in... ')
            for i in range(3, 0, -1):
                print(f'\r{i}', end="")
                time.sleep(1)
            break    

# calls the draw_map() method for robot_map to display the pyplot map
def display_map():
    os.system('cls||clear')
    print('MAP\n')
    robot_map.print_robot_locations()
    robot_map.print_paths()
    robot_map.draw_map()
    input('\npress enter to exit')
    return

# moves the robots to their destinations and displays the pyplot map
def simulation():
    os.system('cls||clear')
    print('MOVING THE ROBOTS...\n')
    for i in range(3, 0 , -1):
        print(f'\r{i}', end='')
        time.sleep(1)
    os.system('cls||clear')
    print('MAP\n')
    robot_map.move_robots()
    robot_map.print_robot_locations()
    robot_map.print_paths()
    robot_map.draw_map()
    input('\npress enter to exit')
    return

# prompts the user for input that allows them to modify the map
def command_line():
    os.system('cls||clear')
    print('COMMAND LINE\n')
    while True:
        # prompt user for their command and split the string into an array of arguments
        command = input('Enter your system command:\n').split()
        if len(command) == 0:
            print('You did not enter a command, try again.')
            continue

        # match the first argument to a command
        match command[0]:
            case 'help':
                command_list()
                os.system('cls||clear')
            case 'exit':
                return
            case 'print':
                # check if print command has a valid number of arguments
                if len(command) != 2:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue

                # match second argument to printable list
                match command[1]:
                    case 'locations':
                        robot_map.print_locations()
                    case 'robots':
                        robot_map.print_robots()
                    case 'paths':
                        robot_map.print_paths()
                    case 'robot-locations':
                        robot_map.print_robot_locations()
                    case _:
                        print(f'\n{command[1]} is not a valid list.\n')
            case 'location':
                robot_map.add_location(command)
            case 'robot':
                robot_map.add_robot(command)
            case 'move':
                robot_map.change_destination(command)
            case 'path':
                robot_map.add_path(command)
            case 'remove':
                robot_map.remove_element(command)
            case _:
                print('Invalid Command, use "help" for more info.\n')

# prints a list of the system commands available to the user for map modification
def command_list():
    os.system('cls||clear')
    print('SYSTEM COMMANDS\n')
    print('''
location <name> <x> <y> ........ Creates a new location named with the name "name" at (x, y) on the map
                                 at the location (x, y). If the location already exists, the system does nothing. Locations
                                 and robots cannot have the same names. Coordinates must be in whole integers.

remove <name> .................. Removes the given robot or location, if it exists.
             
remove <start> <end> ........... Removes the given path, if it exists.
             
path <start> <end> ............. Creates a directed path from start location to end location, if both locations exist. Paths are required for
                                 travel between locations. Robots cannot teleport.
             
robot <name> <start> <end> ..... Creates a robot with the name "name" and puts it on the map at the start location
                                 with the destination at the end location. If a path between these locations doesn't already exist,
                                 the system will automatically create one.

print <list> ................... Prints the given list to the screen. <list> could be "locations" or "robots" or "paths" or "robot-locations" which 
                                 shows which robots are at which locations on the map.

move <robot> <location> ........ Modifies the given robot's destination to the given location so that the next time you run the simulation,
                                 that robot will move to the given location. If there is no path between the robot's current location and its
                                 destination, the system will automaticaly create one.

exit ........................... Exits the system command line.
             
help ........................... Prints out the command list.

''')
    input('press enter to exit')
    return

# driver method, calls login and acts as the main menu for the software system
def main():
    login()
    
    while True:
        os.system('cls||clear')
        print('''MAIN MENU

1 - Display Map
2 - Run Simulation
3 - System Command Line
4 - System command List
5 - Quit\n''')

        # prompt user for their menu selection
        choice = input('What would you like to do?\n')

        # match choice to menu option
        match choice:
            case '1': 
                display_map()
            case '2':
                simulation()
            case '3':
                command_line()
            case '4':
                command_list()
            case '5':
                break
            case _:
                print('Invalid option, try again.')
                time.sleep(1)
    
main()