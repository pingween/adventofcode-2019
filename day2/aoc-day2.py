# import pathlib to use correct file paths in Windows
from pathlib import Path

# adding the "dayX" folder is needed for VS Code,
# somehow the debugger thinks the path is for the workspace not the actual file
day = 2
inputfilepath = Path.cwd() / "day{0}/aoc-day{0}-input.txt".format(day)

# print(Path.cwd(), inputfilepath, end='\n')

# First part ========================================================

with open(inputfilepath, "r") as inputfile:
    intcode = inputfile.read().split(',')

for i in len (intcode):