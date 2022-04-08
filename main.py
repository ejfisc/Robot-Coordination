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
        command = input('Enter your system command:\n')
        # TODO: evaluate user commands
        if command == 'help':
            command_list()
            os.system('cls||clear')
        elif command == 'exit':
            return

def command_list():
    os.system('cls||clear')
    print('SYSTEM COMMANDS\n')
    print('location name, (x, y) - Creates a new location named with the name "name" at (x, y) on the map\n\
           \t\tat the location (x, y). If the location already exists, the system does nothing. Locations\n\
           \t\tand robots cannot have the same names.\n')
    print('remove name - Removes the given robot or location, if it exists.\n')
    print('remove (start, end) - Removes the given path, if it exists.\n')
    print('path (start, end) - Creates a directed path from start location to end location, if both\n\
           \t    locations exist.\n')
    print('robot name, (start, end) - Creates a robot with the name "name" and put it on the map at start\n\
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
    
       
main()