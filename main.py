#! python3
# main.py - main driver program for the robot coordination system

import os, time, map_data

# users dictionary - username: password
users = {'Ethan': 'Fischer', 'user': 'pass', 'logi': 'tech', 'test': 'python'}

# robots dictionary - name: (start, end)
robots = {'r1': ('start', 'end'), 'r2': ('north', 'south'), 'r3': ('east', 'west')}

# locations dictionary - name: (x, y)
locations = {'nw': (0, 0), 'ne': (15, 0), 'se': (15, 15), 'sw': (0, 15)}

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
    print('MAP')
    print(robot_map)
    input('press enter to exit')
    return

def simulation():
    os.system('cls||clear')
    print('SIMULATED MAP')
    # TODO: draw the map after simulation
    input('press enter to exit')
    return
    
def command_line():
    os.system('cls||clear')
    print('COMMAND LINE')
    while True:
        command = input('Enter your system command:\n').split()
        match command[0]:
            case 'help':
                command_list()
                os.system('cls||clear')
            case 'exit':
                return
            case 'location':
                if len(command) != 4:
                    print('Invalid Command')
                    continue
            case 'robot':
                if len(command) != 4:
                    print('Invalid Command')
                    continue
            case 'path':
                pass
            case 'remove':
                if len(command) < 2 or len(command) > 3:
                    print('Invalid Command')
                    continue
                elif len(command) == 2:
                    if command[1] in robots:
                        robots.pop(command[1])
                        print(f'Robot {command[1]} successfully removed.')
                        print('\nRobots:')
                        for k, v in robots.items():
                            print(f'{k}: {v}')
                        print()
                    elif command[1] in locations:
                        locations.pop(command[1])
                        print(f'Location {command[1]} successfully removed.')
                        print('\nLocations:')
                        for k, v in locations.items():
                            print(f'{k}: {v}')
                        print()
                    else:
                        print(f'{command[1]} is not a robot or location on this map.')
                        continue
            case _:
                print('Invalid Command')

def command_list():
    os.system('cls||clear')
    print('SYSTEM COMMANDS\n')
    print('location name x y - Creates a new location named with the name "name" at (x, y) on the map\n\
           \t\tat the location (x, y). If the location already exists, the system does nothing. Locations\n\
           \t\tand robots cannot have the same names.\n')
    print('remove name - Removes the given robot or location, if it exists.\n')
    print('remove start end - Removes the given path, if it exists.\n')
    print('path start end - Creates a directed path from start location to end location, if both\n\
           \t    locations exist.\n')
    print('robot name start end - Creates a robot with the name "name" and put it on the map at start\n\
           \t\t   with the destination at end.\n')
    print('exit - Exits the system command line.\n')
    print('help - Prints out the command list.\n')
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
    
       
command_line()