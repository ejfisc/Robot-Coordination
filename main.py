#! python3
# main.py - main driver program for the robot coordination system

import os, time, map_data

# users dictionary - username: password
users = {'Ethan': 'Fischer', 'user': 'pass', 'logi': 'tech', 'test': 'python'}

# create the map
rows, cols = (15, 15)
robot_map = map_data.Robot_Map(rows, cols)

def login():
    os.system('cls||clear')
    print('LOG IN\n')
    while True:
        username = input('Enter username:   ')
        password = input('Enter password:   ')
        if username not in users.keys() or users.get(username) != password:
            print('Username or password is incorrect, try again.')
            continue
        if users.get(username) == password:
            os.system('cls||clear')
            print(f'Welcome, {username}')
            print('Going to home screen in... ')
            for i in range(3, 0, -1):
                print(f'\r{i}', end="")
                time.sleep(1)
            break    


def display_map():
    os.system('cls||clear')
    print('MAP\n')
    print(robot_map)
    input('press enter to exit')
    return

def simulation():
    os.system('cls||clear')
    print('SIMULATED MAP\n')
    # TODO: draw the map after simulation
    input('press enter to exit')
    return

def command_line():
    os.system('cls||clear')
    print('COMMAND LINE\n')
    while True:
        command = input('Enter your system command:\n').split()
        if len(command) == 0:
            print('You did not enter a command, try again.')
            continue
        match command[0]:
            case 'help':
                command_list()
                os.system('cls||clear')
            case 'exit':
                return
            case 'print':
                if len(command) != 2:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue
                match command[1]:
                    case 'locations':
                        robot_map.print_locations()
                    case 'robots':
                        robot_map.print_robots()
                    case 'paths':
                        robot_map.print_paths()
                    case _:
                        print(f'\n{command[1]} is not a valid list.\n')
            case 'location':
                robot_map.add_location(command)
            case 'robot':
                robot_map.add_robot(command)
            case 'path':
                robot_map.add_path(command)
            case 'remove':
                robot_map.remove_element(command)
            case _:
                print('Invalid Command, use "help" for more info.\n')

def command_list():
    os.system('cls||clear')
    print('SYSTEM COMMANDS\n')
    print('''
location <name> <x> <y> - Creates a new location named with the name "name" at (x, y) on the map
                          at the location (x, y). If the location already exists, the system does nothing. Locations
                          and robots cannot have the same names.

remove <name> - Removes the given robot or location, if it exists.
             
remove <start> <end> - Removes the given path, if it exists.
             
path <start> <end> - Creates a directed path from start location to end location, if both locations exist.
             
robot <name> <start> <end> - Creates a robot with the name "name" and put it on the map at start
                             with the destination at end.

print <list> - Prints the given list to the screen. <list> could be "locations" or "robots" or "paths"

exit - Exits the system command line.
             
help - Prints out the command list.

''')
    input('press enter to exit')
    return

def main():
    login()
    
    while True:
        os.system('cls||clear')
        print('MAIN MENU\n')
        print('1 - Display Map')
        print('2 - Run Simulation')
        print('3 - System Command Line')
        print('4 - System Command List')
        print('5 - Quit\n')
        print('What would you like to do?')
        choice = input()
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