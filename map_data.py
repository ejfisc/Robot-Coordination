#! python3
# robot_map.py - data class for robot map
import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
class Robot_Map():

    # robots dictionary - name: (start, end)
    robots = {}
    # locations dictionary - name: (x, y)
    locations = {} 
    # paths list - (start, end)
    paths = []
    # robot-location relationship dictionary - location: [robots]
    robot_locations = {}
    # location annotation list
    location_annotations = []
    # path annotation list
    path_annotations = []
    # robot annotations list
    robot_annotations = []

    # constructor
    def __init__(self, width, height, fig, ax) -> None:
        self.width = width
        self.height = height
        self.fig = fig
        self.ax = ax

    # displays the map in a pyplot window
    def draw_map(self) -> None:
        plt.show(block=False)

    # handles mouse click events on the map, when the user clicks on a location, a box pops up displaying the robots at that location
    def on_click(self, event) -> None:
        # get the click coordinates
        click_coords = (event.xdata, event.ydata)
        temp_locations = self.location_annotations.copy()
        temp_robots = self.robot_annotations.copy()

        # do nothing and return if click was outside of figure
        if event.xdata is None or event.ydata is None:
            return

        # loop through each location annotation to find the location clicked on
        for ann in temp_locations:
            if self.inside_bubble(click_coords, ann.xy):
                # check for pre existing robot list annotation to remove
                for robot_list in temp_robots:
                    if self.inside_bubble(click_coords, ann.xy):
                        robot_list.remove()
                        self.robot_annotations.remove(robot_list)
                        plt.draw()
                        return

                # get the list of robots at that location
                robots = ', '.join(self.robot_locations.get(ann._text))

                # display the robots
                new_robot_list = self.ax.annotate(robots, xy=click_coords, xycoords='data', va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))
                self.robot_annotations.append(new_robot_list)
                plt.draw()
                return
            
    # adds a path to the map, returns True if a path was succesfully added, False otherwise
    def add_path(self, command) -> bool:
        # check arguments
        if len(command) != 3:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False

        # check for valid locations
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
            # add path to paths list
            self.paths.append((command[1], command[2]))

            # create a new annotation for path and add it to path annotation list
            start = self.locations.get(command[1])
            start_coords = (int(start[0]), int(start[1]))
            end = self.locations.get(command[2])
            end_coords = (int(end[0]), int(end[1]))
            new_path = self.ax.annotate('', xy=end_coords, xytext=start_coords, xycoords='data', arrowprops=dict(arrowstyle="->", shrinkA=15, shrinkB=15))
            plt.draw()
            self.path_annotations.append(new_path)

            # print result and return
            print(f'The path ({command[1]} -> {command[2]}) was successfully created.\n')
            return True

    # adds a location to the map, returns True if a location was successfully added, False otherwise
    def add_location(self, command) -> bool:
        # check arguments
        if len(command) != 4:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False

        # check for preexisting robot or location with the same name
        if command[1] in self.robots:
            print('Locations cannot have the same name as robots.\n')
            return False
        elif command[1] in self.locations:
            print(f'{command[1]} already exists.\n')
            return False

        # check for valid coordinates
        if int(command[2]) < 0 or int(command[2]) > self.width:
            print(f'{command[2]} is outside the map limits: {self.width} x {self.height}\n')
            return False
        elif int(command[3]) < 0 or int(command[3]) > self.height:
            print(f'{command[3]} is outside the map limits: {self.width} x {self.height}\n')
            return False

        # check if location already exists at those coordinates
        if (command[2], command[3]) in self.locations.values():
            for k, v in self.locations.items():
                # update each path with that location
                if v == (command[2], command[3]):
                    self.locations.pop(k)
                    for path in self.paths:
                        if k == path[0]:
                            path[0] = command[1]
                        elif k == path[1]:
                            path[1] = command[1]
                    break
                
            # update locations dictionary
            self.locations.update({command[1]: (command[2], command[3])})

            # update location_annotations list and redraw the map
            for ann in self.location_annotations:
                if ann.xy == (int(command[2]), int(command[3])):
                    ann.set_text(command[1])
                    plt.draw()
            
            # print result and return
            print(f'Location at ({command[2]}, {command[3]}) updated to {command[1]}.\n')
            return True
        else:
            # update locations dictionary
            self.locations.update({command[1]: (command[2], command[3])})
            self.robot_locations.update({command[1]: []})

            # create a new annotation for the location and redraw the map
            new_location = self.ax.annotate(command[1], xy=(int(command[2]), int(command[3])), xycoords='data', va="center", ha="center", bbox=dict(boxstyle="round", fc="w"))
            plt.draw()
            self.location_annotations.append(new_location)

            # print result and return
            print(f'Location {command[1]} created at ({command[2]}, {command[3]}).\n')
            return True

    # adds a robot to the map, returns True if a robot was succesfully added, False otherwise
    def add_robot(self, command) -> bool:
        # check arguments
        if len(command) != 4:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False

        # check for preexisting robot or location with the same name
        if command[1] in self.locations:
            print('Robots cannot have the same name as locations.\n')
            return False
        elif command[1] in self.robots:
            print(f'{command[1]} already exists.\n')
            return False
        
        # check for valid location names
        if command[2] not in self.locations or command[3] not in self.locations:
            print('Invalid location.\n')
            return False
        
        # create new path for robot to travel on if it doesn't already exist
        if (command[2], command[3]) not in self.paths:
            # call add_path with path command to create a new path, update robots dictionary and add robot to location
            self.add_path(['path', command[2], command[3]])
            self.robots.update({command[1]: (command[2], command[3])})
            self.robot_locations.get(command[2]).append(command[1])

            # print result and return
            print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            return True
        else:
            # update robots dictionary and add robot to location
            self.robots.update({command[1]: (command[2], command[3])})
            self.robot_locations.get(command[2]).append(command[1])

            # print result and return
            print(f'Robot {command[1]} has been created at {command[2]} and will move to {command[3]}.\n')
            return True

    # removes an element from the map, return True if element was succesfully removed, False otherwise
    def remove_element(self, command) -> bool:
        # check arguments
        if len(command) < 2 or len(command) > 3:
            print('Invalid Number of Arguments, use "help" for more info.\n')
            return False
        
        # if there are 2 arguments, remove robot or location
        if len(command) == 2:
            # check if element is a robot
            if command[1] in self.robots:
                # remove robot from robots dictionary
                self.robots.pop(command[1])

                # remove any instances of the robot in robot_locations
                temp_list = self.robot_locations.values().copy()
                for robots in temp_list:
                    if command[1] in robots:
                        robots.remove(command[1])
                
                # print result, print a list of the remaining robots, and return
                print(f'Robot {command[1]} successfully removed.\n')
                self.print_robots()
                return True
            
            # check if element is a location
            if command[1] in self.locations:
                # first remove any path annotations that this location is in
                location = self.locations.get(command[1])
                coords = (int(location[0]), int(location[1]))
                temp_list = self.path_annotations.copy()
                for ann in temp_list:
                    if ann.xyann == coords or ann.xy == coords:
                        self.path_annotations.remove(ann)
                        ann.remove()
                        plt.draw()
                
                # remove location from locations dictionary
                self.locations.pop(command[1])

                # remove location from location annotations
                temp_list = self.location_annotations.copy()
                for ann in temp_list:
                    if ann._text == command[1]:
                        self.location_annotations.remove(ann)
                        ann.remove()
                        plt.draw()
                
                # remove the location from robot_locations
                self.robot_locations.pop(command[1])
                
                # print result and list of remaining locations
                print(f'Location {command[1]} successfully removed.\n')
                self.print_locations()

                # remove any instances of the location in paths
                temp_list = self.paths.copy()
                for path in temp_list:
                    if command[1] in path:
                        self.paths.remove(path)
                        print(f'The path ({path[0]}, {path[1]}) which contains {command[1]} has been removed.')
                print()
                return True
            else:
                print(f'{command[1]} is not a robot or location on this map.\n')
                return False
        
        # if there are 3 arguments, remove a path
        if len(command) == 3:
            # check for valid locations
            if command[1] not in self.locations:
                print(f'{command[1]} is not a location on this map.\n')
                return False
            elif command[2] not in self.locations:
                print(f'{command[2]} is not a location on this map.\n')
                return False
            else:
                # remove path from path annotations and redraw map
                temp_list = self.path_annotations.copy()
                start = self.locations.get(command[1])
                end = self.locations.get(command[2])
                start_coords = (int(start[0]), int(start[1]))
                end_coords = (int(end[0]), int(end[1]))
                for ann in temp_list:
                    if ann.xyann == start_coords and ann.xy == end_coords:
                        self.path_annotations.remove(ann)
                        ann.remove()
                        plt.draw()
                
                # remove path from paths list
                self.paths.remove((command[1], command[2]))

                # print result, list of remaining paths, and return
                print(f'Path ({command[1]}, {command[2]}) successfully removed.\n')
                self.print_paths()
                return True

    # prints a list of the locations
    def print_locations(self) -> None:
        print('\nLocations:')
        for k, v in self.locations.items():
           print(f'{k}: ({v[0]}, {v[1]})')
        print()

    # prints a list of the robots
    def print_robots(self) -> None:
        print('\nRobots:')
        for k, v in self.robots.items():
            print(f'{k}: ({v[0]} -> {v[1]})')
        print()

    # prints a list of the paths
    def print_paths(self) -> None:
        print('\nPaths:')
        for path in self.paths:
            print(f'({path[0]} -> {path[1]})')
        print()

    # prints a list of the locations and which robots are at each location
    def print_robot_locations(self) -> None:
        print('\nRobot-Locations:')
        for k, v in self.robot_locations.items():
                print(f'{k}: ', end='')
                print(*v, sep=', ')
        print()

    # returns True if mouse click coordinates are within the boundaries of the location coordinates
    def inside_bubble(self, click_coords, location_coords) -> bool:
        clickx, clicky = click_coords[0], click_coords[1]
        locationx, locationy = location_coords[0], location_coords[1]
        # check x coordinates
        if clickx < (locationx-0.6) or clickx > (locationx+0.6):
            return False
        # check y coordinates
        if clicky < (locationy-0.4) or clicky > (locationy+0.4):
            return False
        # click is within 1 point of the location coordinates
        return True
        