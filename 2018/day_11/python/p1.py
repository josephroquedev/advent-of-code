#!/usr/bin/env python3

serial_number = 7511
grid_size = 300

power_levels = {}
fuel_cells = {}

def power_level(x, y):
    return (((((x + 10) * y + serial_number) * (x + 10)) % 1000) // 100) - 5

def power_of_cell(x, y):
    power = 0
    for xx in range(3):
        for yy in range(3):
            power += power_levels[(x - xx, y - yy)]
    return power

for x in range(1, grid_size + 1):
    for y in range(1, grid_size + 1):
        level = power_level(x,y)
        power_levels[(x, y)] = level
        if x >= 3 and y >= 3:
            fuel_cells[(x, y)] = power_of_cell(x, y)

max_fuel_cell = max(fuel_cells, key=fuel_cells.get)
print('The fuel cell of size 3 with maximum power is:', (max_fuel_cell[0] - 2, max_fuel_cell[1] - 2))
