# Sensor Parser for SmartWash

## Windows Installation Process: 
1. Install Anaconda from the following link: [https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)
2. Allow it to install Python and set up the paths
3. Download the project from the github, either by clicking ```code``` and install as zip (then extracting it) or using the terminal command                   ```git clone https://github.com/sewageseaweed/SensorParser.git```
4. Launch the Anaconda Prompt (Anaconda 3)
5. Navigate to where you installed the folder using the ```cd``` command. Use the ```dir``` command to get list of files/directories in your current directory.
6. Run the following command ```conda env create -f environment.yml```
7. Launch the application by running ```python sensorGUI.py```
8. A GUI should open in a few seconds.

## Linux/MacOS Installation Process:
1. Almost entireley the same as the windows installation process. However, you can just use the builtin command line/terminal instead of the Anaconda Prompt.
2. If you use the builtin command line/terminal, you can use the ```ls``` command to get a list of files/directories in your current directory instead of using the ```dir``` command.

## Notes:
- Do not exit until the "Current Status" window says "Finished! You may exit!". Parsing sometimes takes awhile and you don't want to lose all your progress before it finishes...
- 3 months seem to be ideal.
- I ran this on a powerful machine (RTX 3090, Ryzen 9 5900x, and on a SSD) so it may take longer on less powerful machines. 
