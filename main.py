#! python3
# main.py - main driver program for the robot coordination system

import os, time, map_data

# users dictionary - username: password
users = {'Ethan': 'Fischer', 'user': 'pass', 'logi': 'tech', 'test': 'python'}

# robots dictionary - name: (start, end)
robots = {}

# locations dictionary - name: (x, y)
locations = {}

# paths list - (start, end)
paths = [] 

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
                        print('\nLocations:')
                        for k, v in locations.items():
                            print(f'{k}: ({v[0]}, {v[1]})')
                        print()
                    case 'robots':
                        print('\nRobots:')
                        for k, v in robots.items():
                            print(f'{k}: ({v[0]}, {v[1]})')
                        print()
                    case 'paths':
                        print('\nPaths:')
                        for path in paths:
                            print(f'({path[0]}, {path[1]})')
                        print()
                    case _:
                        print(f'\n{command[1]} is not a valid list.\n')
            case 'location':
                if len(command) != 4:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue
                if command[1] in robots:
                    print('Locations cannot have the same name as robots.\n')
                    continue
                elif command[1] in locations:
                    print(f'{command[1]} already exists.\n')
                    continue
                elif int(command[2]) < 0 or int(command[2]) > cols:
                    print(f'{command[2]} is outside the map limits: {cols} x {rows}\n')
                elif int(command[3]) < 0 or int(command[3]) > rows:
                    print(f'{command[3]} is outside the map limits: {cols} x {rows}\n')
                elif (command[2], command[3]) in locations.values():
                    for k, v in locations.items():
                       if v == (command[2], command[3]):
                            locations.pop(k)
                            break
                    locations.update({command[1]: (command[2], command[3])})
                    print(f'Location at ({command[2]}, {command[3]}) updated to {command[1]}.\n')
                else:
                    locations.update({command[1]: (command[2], command[3])})
                    print(f'Location {command[1]} created at ({command[2]}, {command[3]}).\n')
            case 'robot':
                if len(command) != 4:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue
                if command[1] in locations:
                    print('Robots cannot have the same name as locations.\n')
                elif command[1] in robots:
                    print(f'{command[1]} already exists.\n')
                elif command[2] not in locations or command[3] not in locations:
                    print('Invalid location.\n')
                else:
                    robots.update({command[1]: (command[2], command[3])})
                    print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            case 'path':
                if len(command) != 3:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue
                if command[1] not in locations:
                    print(f'{command[1]} is not a location on this map.\n')
                elif command[2] not in locations:
                    print(f'{command[2]} is not a location on this map.\n')
                elif (command[1], command[2]) in paths:
                    print(f'The path ({command[1]}, {command[2]}) already exists.\n')
                else:
                    paths.append((command[1], command[2]))
                    print(f'The path ({command[1]}, {command[2]}) was successfully created.\n')
            case 'remove':
                if len(command) < 2 or len(command) > 3:
                    print('Invalid Number of Arguments, use "help" for more info.\n')
                    continue
                elif len(command) == 2:
                    if command[1] in robots:
                        robots.pop(command[1])
                        print(f'Robot {command[1]} successfully removed.\n')
                        print('\nRobots:')
                        for k, v in robots.items():
                            print(f'{k}: {v}')
                        print()
                    elif command[1] in locations:
                        locations.pop(command[1])
                        print(f'Location {command[1]} successfully removed.\n')
                        print('\nLocations:')
                        for k, v in locations.items():
                            print(f'{k}: {v}')
                        print()
                        # remove any instances of the location in paths
                        for path in paths:
                            if command[1] in path:
                                paths.remove(path)
                                print(f'The path ({path[0]}, {path[1]}) which contains {command[1]} has been removed.')
                        print()
                    else:
                        print(f'{command[1]} is not a robot or location on this map.\n')
                        continue
                elif len(command) == 3:
                    if command[1] not in locations:
                        print(f'{command[1]} is not a location on this map.\n')
                    elif command[2] not in locations:
                        print(f'{command[2]} is not a location on this map.\n')
                    else:
                        temp_path = (command[1], command[2])
                        paths.remove(temp_path)
                        print(f'Path ({command[1]}, {command[2]}) successfully removed.\n')
                        print('\nPaths:')
                        for path in paths:
                            print(f'({path[0]}, {path[1]})')
                        print()
            case _:
                print('Invalid Command, use "help" for more info.\n')

def command_list():
    os.system('cls||clear')
    print('SYSTEM COMMANDS')
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