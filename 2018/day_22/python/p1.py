#!/usr/bin/env python3

import re

import os
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = '{}/../{}.txt'.format(SCRIPT_PATH, 'input')


def get_file():
    with open(FILENAME) as f:
        return f.read()


def get_numbers_from_line(line, allow_negatives=True):
    regex = r'-?\d+' if allow_negatives else r'\d+'
    return [int(match) for match in re.findall(regex, line)]


PUZZLE_INPUT = get_numbers_from_line(get_file())
depth = PUZZLE_INPUT[0]
target = (PUZZLE_INPUT[1], PUZZLE_INPUT[2])
mouth = (0, 0)

ROCKY, WET, NARROW = 0, 1, 2

geologic_indices = {
    mouth: 0,
    target: 0,
}


def geologic_index(region):
    if region in geologic_indices:
        return geologic_indices[region]

    x, y = region
    if y == 0:
        index = x * 16807
    elif x == 0:
        index = y * 48271
    else:
        index = erosion_level((x - 1, y)) * erosion_level((x, y - 1))

    geologic_indices[region] = index
    return index


def erosion_level(region):
    index = geologic_index(region)
    return (index + depth) % 20183


def region_type(region):
    erosion = erosion_level(region)
    return erosion % 3


total_risk = sum(region_type((x, y)) for x in range(target[0] + 1) for y in range(target[1] + 1))
print('The total risk for the cave is', total_risk)
