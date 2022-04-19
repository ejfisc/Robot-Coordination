# Robot-Coordination
Assignment 3 for CS 3354 - Software Engineering<br>
Control system for a high-level robot-coordination map.<br>
The system uses the terminal for operations and pyplot to graphically represent the map.
## Contents:
Assignment 1 and 2 documents provided for context<br>
main.py - Driver program for the system, controls the console UI<br>
map_data.py - Controls the matplotlib map UI for this Robot-Coordination system
## Requirements:
Python 3.10+
matplotlib (run 'pip install matplotlib')
## Getting Started:
Run the main.py file using an IDE or 'python main.py' in the terminal. You will be prompted to log in. At the moment, there is no way for the user to 
modify the users in the system, but the default credentials are: <br><br>
username: 'user'<br>
password: 'pass'<br><br>
Logging in will take you to the main menu, where you can display the map, run the simulation, go to the command line, look at a list of system commands, or quit. <br>
When you display the map, a pyplot window will open with the map, **DO NOT CLOSE THIS WINDOW**. If you close the window, you will not be able to reopen it in the system. Simply click away from it, and when you need to see it again, you can choose display map in the main menu and the window with your map will pop back up and reflect any changes you made in the system command line.<br>
Running the simulation will move robots to their destination.<br>
The system command line is where you can make modifications to the map, like adding and removing robots, paths, locations and change a robot's destination. <br>
The list of system commands is essentially the instruction booklet for the system. It walks you through each command, what arguments they take, and how they work. <br>
Quitting stops the program and quits the system entirely. At this moment there is no way to save any progress, so you lose your map and all of its data.
