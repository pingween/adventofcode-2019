# import pathlib to use correct file paths in Windows
from pathlib import Path

# adding the "day1" folder is needed for VS Code,
# somehow the debugger thinks the path is for the workspace not the actual file
inputfilepath = Path.cwd() / "day1/aoc-day1-input.txt"

# print(Path.cwd(), inputfilepath, end='\n')

# First part ========================================================

fuel = 0
with open(inputfilepath, "r") as inputfile:
    for line in inputfile:
        # adding fuel line by line given the module size divided by 3, rounded down and -2
        fuel += int(line) // 3 - 2

print('Fuel needed without calculating the fuel in:', fuel)

# Second Part without recursion =====================================

fuel = 0

with open(inputfilepath, "r") as inputfile:
    for line in inputfile:
        size = int(line)
        # repeating the rocket equation until the needed fuel is 0
        while size > 6:
            # print(size)
            # the equation gives the fuel's mass which needs it's own fuel
            size = size // 3 - 2
            fuel += size

print('Fuel needed with the fuel\'s mass in mind:', fuel)


# Second Part with recursion ========================================

fuel = 0

def calc_fuel(size):
    
    # print(size)
    if size > 8:
        size = size // 3 - 2
        return size + calc_fuel(size)
    else:
        return 0

# fuel = calc_fuel(100756)

def calc_fuel2(size):
    size = size // 3 - 2
    # print(size)
    if size // 3 - 2 >= 0:
        return size + calc_fuel2(size)
    else:
        return size

# print(calc_fuel2(1969))
# print(calc_fuel2(100756))

with open(inputfilepath, "r") as inputfile:
  for line in inputfile:
      fuel += calc_fuel(int(line))

print('Fuel needed with the fuel\'s mass in mind (recursive):', fuel)