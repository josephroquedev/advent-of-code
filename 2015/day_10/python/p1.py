#!/usr/bin/env python3

import re

# Input from the site
PUZZLE_INPUT = '1113122113'

# Apply the process 40 times
for i in range(40):
    puzzle_output = ''

    # Get character repeated at start, number of times its repeated and add to output
    while len(PUZZLE_INPUT) > 0:
        digits = re.search(r'(\d)\1*', PUZZLE_INPUT)
        PUZZLE_INPUT = PUZZLE_INPUT[len(digits.group(0)):]
        puzzle_output = puzzle_output + str(len(digits.group(0))) + str(digits.group(0)[:1])

    # Update input to iterate
    PUZZLE_INPUT = puzzle_output

# Update final output
puzzle_output = PUZZLE_INPUT

# Print the final length of the output
print('The length of the result is', len(puzzle_output))
