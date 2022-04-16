#! python3
# robot_map.py - data class for robot map

class Robot_Map():

    # robots dictionary - name: (start, end)
    robots = {}

    # locations dictionary - name: (x, y)
    locations = {}

    # paths list - (start, end)
    paths = []      

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.data = [['*']*height]*width

    def __str__(self) -> str:
        data = self.data
        map_string = ''
        for row in data:
            for col in row:
                map_string += col + '  '
            map_string += '\n\n'
        return map_string
            
    def add_path(self, command) -> bool:
        if len(command) != 3:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        if command[1] not in self.locations:
            print(f'{command[1]} is not a location on this map.\n')
            return False
        elif command[2] not in self.locations:
            print(f'{command[2]} is not a location on this map.\n')
            return False
        elif (command[1], command[2]) in self.paths:
            print(f'The path ({command[1]}, {command[2]}) already exists.\n')
            return False
        else:
            self.paths.append((command[1], command[2]))
            print(f'The path ({command[1]} -> {command[2]}) was successfully created.\n')
            return True

    def add_location(self, command) -> bool:
        if len(command) != 4:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        if command[1] in self.robots:
            print('Locations cannot have the same name as robots.\n')
            return False
        elif command[1] in self.locations:
            print(f'{command[1]} already exists.\n')
            return False
        elif int(command[2]) < 0 or int(command[2]) > self.width:
            print(f'{command[2]} is outside the map limits: {self.width} x {self.height}\n')
        elif int(command[3]) < 0 or int(command[3]) > self.height:
            print(f'{command[3]} is outside the map limits: {self.width} x {self.height}\n')
        elif (command[2], command[3]) in self.locations.values():
            for k, v in self.locations.items():
                if v == (command[2], command[3]):
                    self.locations.pop(k)
                    break
            self.locations.update({command[1]: (command[2], command[3])})
            print(f'Location at ({command[2]}, {command[3]}) updated to {command[1]}.\n')
            return True
        else:
            self.locations.update({command[1]: (command[2], command[3])})
            print(f'Location {command[1]} created at ({command[2]}, {command[3]}).\n')
            return True

    def add_robot(self, command) -> bool:
        if len(command) != 4:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        if command[1] in self.locations:
            print('Robots cannot have the same name as locations.\n')
            return False
        elif command[1] in self.robots:
            print(f'{command[1]} already exists.\n')
            return False
        elif command[2] not in self.locations or command[3] not in self.locations:
            print('Invalid location.\n')
            return False
        else:
            self.robots.update({command[1]: (command[2], command[3])})
            print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            return True

    def remove_element(self, command) -> bool:
        if len(command) < 2 or len(command) > 3:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        elif len(command) == 2:
            if command[1] in self.robots:
                self.robots.pop(command[1])
                print(f'Robot {command[1]} successfully removed.\n')
                self.print_robots()
                return True
            elif command[1] in self.locations:
                self.locations.pop(command[1])
                print(f'Location {command[1]} successfully removed.\n')
                self.print_locations()
                # remove any instances of the location in paths
                for path in self.paths:
                    if command[1] in path:
                        self.paths.remove(path)
                        print(f'The path ({path[0]}, {path[1]}) which contains {command[1]} has been removed.')
                print()
                return True
            else:
                print(f'{command[1]} is not a robot or location on this map.\n')
                return False
        elif len(command) == 3:
            if command[1] not in self.locations:
                print(f'{command[1]} is not a location on this map.\n')
                return False
            elif command[2] not in self.locations:
                print(f'{command[2]} is not a location on this map.\n')
                return False
            else:
                temp_path = (command[1], command[2])
                self.paths.remove(temp_path)
                print(f'Path ({command[1]}, {command[2]}) successfully removed.\n')
                self.print_paths()
                return True

    def print_locations(self) -> None:
        print('\nLocations:')
        for k, v in self.locations.items():
           print(f'{k}: ({v[0]}, {v[1]})')
        print()

    def print_robots(self) -> None:
        print('\nRobots:')
        for k, v in self.robots.items():
            print(f'{k}: ({v[0]} -> {v[1]})')
        print()

    def print_paths(self) -> None:
        print('\nPaths:')
        for path in self.paths:
            print(f'({path[0]} -> {path[1]})')
        print()