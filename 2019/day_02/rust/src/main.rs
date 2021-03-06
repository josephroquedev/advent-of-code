use opcode_computer::Program;

/* Part 1
================================================= */

fn part_one(input: String) {
    let result = Program::from_str(&input).set(1, 12).set(2, 2).run().get(0);

    println!("The value at position 0 is {}", result);
}

/* Part 2
================================================= */

fn part_two(input: String) {
    for noun in 0..99 {
        for verb in 0..99 {
            let result = Program::from_str(&input)
                .set(1, noun)
                .set(2, verb)
                .run()
                .get(0);

            if result == 19690720 {
                println!("100 * noun + verb is {}", 100 * noun + verb);
                return;
            }
        }
    }
}

/* Main + Input
================================================= */

use aoc_util::{aoc, AOCParams};

fn main() {
    aoc(&part_one, &part_two, AOCParams::new(false, None));
}
