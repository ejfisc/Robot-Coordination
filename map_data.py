#! python3
# robot_map.py - data class for robot map

class Robot_Map():

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
            

