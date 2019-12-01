# import pathlib to use correct file paths in Windows
from pathlib import Path

# adding the "day1" folder is needed for VS Cpde, somehow the debugger thinks the path is for the workspace not the actual file 
inputfilepath = Path.cwd() / "day1/aoc-day1-input.txt"

# print(Path.cwd(), inputfilepath, end='\n')

fuel = 0

with open(inputfilepath, "r") as inputfile:
    for line in inputfile:
        # adding fuel line by line given the module size divided by 3, rounded down and -2
        fuel += int(line) // 3 - 2

print(fuel)