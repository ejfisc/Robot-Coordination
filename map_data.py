#! python3
# robot_map.py - data class for robot map
class Robot_Map():

    # robots dictionary - name: (start, end)
    robots = {'r1': ('nw', 'center'), 'r2': ('sw', 'ne'), 'r3': ('test2', 'center'), 'r4': ('sw', 'test')}

    # locations dictionary - name: (x, y)
    locations = {'nw': (1, 1), 'ne': (15, 1), 'se': (15, 15), 'sw': (1, 15), 'center': (7, 7), 'test': (8, 3), 'test2': (9, 5)}

    # paths dictionary - (start, end)
    paths = [('nw', 'center'), ('center', 'se'), ('sw', 'ne'), ('ne', 'se'), ('test2', 'center'), ('sw', 'test')]

    # robot-location relationship dictionary - location: [robots]
    robot_locations = {'nw': ['r1'], 'ne': [], 'se': [], 'sw': ['r2', 'r4'], 'center': [], 'test': [], 'test2': ['r3']}

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.data = []
            

    def __str__(self) -> str:
        self.fill_map()
        map_string = ''
        for row in self.data:
            for col in row:
                map_string += col
            map_string += '\n\n\n'
        return map_string

    def fill_map(self):
        data = []
        for i in range(self.width+1):
            col = []
            for j in range(self.height+1):
                if j == 0 and i == 0:
                    col.append(' \t')
                elif j == 0:
                    col.append(str(i) + '\t')
                elif i == 0:
                    col.append(str(j) + '\t')
                else: 
                    col.append('_\t')
            data.append(col)
        for k, v in self.locations.items():
            (x, y) = (v[1], v[0])
            num_robots = len(self.robot_locations.get(k))
            data[x][y] = f'X{num_robots}\t'
        self.data = data
            
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
                    for path in self.paths:
                        if k == path[0]:
                            path[0] = command[1]
                        elif k == path[1]:
                            path[1] = command[1]
                    break
            self.locations.update({command[1]: (command[2], command[3])})
            print(f'Location at ({command[2]}, {command[3]}) updated to {command[1]}.\n')
            return True
        else:
            self.locations.update({command[1]: (command[2], command[3])})
            self.robot_locations.update({command[1]: []})
            self.data[int(command[2])][int(command[3])] = 'X0\t'
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
        elif (command[2], command[3]) not in self.paths:
            self.add_path(['path', command[2], command[3]])
            self.robots.update({command[1]: (command[2], command[3])})
            self.robot_locations.get(command[2]).append(command[1])
            print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            return True
        else:
            self.robots.update({command[1]: (command[2], command[3])})
            self.robot_locations.get(command[2]).append(command[1])
            print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            return True

    def remove_element(self, command) -> bool:
        if len(command) < 2 or len(command) > 3:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        elif len(command) == 2:
            if command[1] in self.robots:
                self.robots.pop(command[1])
                # remove any instances of the robot in robot_locations
                for robots in self.robot_locations.values():
                    if command[1] in robots:
                        robots.remove(command[1])
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
                # remove any instances of the location in robot_locations
                for location in self.robot_locations.keys():
                    if command[1] == location:
                        self.robot_locations.pop(location)
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

    def print_robot_locations(self) -> None:
        print('\nRobot-Locations:')
        for k, v in self.robot_locations.items():
                print(f'{k}: ', end='')
                print(*v, sep=', ')
        print()