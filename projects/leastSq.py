#! /usr/bin/env python3

import os
import re
from typing import TextIO, Generator

class LeastSquares:
    def __init__(self, readings, step, filename):
        self.readings = readings
        self.step = step
        self.filename = filename

    def gen_file_name(self, core):
        return self.filename.replace(".txt", f"-core-{core:02d}.txt")

    def linear_interpolation_loop(self):
        for i, reading in enumerate(self.readings):
            core_file_name = self.gen_file_name(i)

            try:
                # Open the file in append mode if it exists, else create a new one
                mode = 'a' if os.path.exists(core_file_name) else 'w'

                with open(core_file_name, mode) as out:
                    ls = self.least_squares_approximation(self.step, reading)

                    out.write(f"{0:6d} <= x <= {(len(reading) - 1) * self.step:6d} ; "
                              f"y = {ls[1]:10.4f} + {ls[0]:10.4f} x ; least-squares \n")
            except IOError as ex:
                print(f"Error creating output file for core {i}: {ex}")

    def least_squares_approximation(self, step, arr):
        a1 = len(arr)
        a2 = self.gen_a2(step, arr)
        a3 = self.gen_a3(arr)

        b1 = a2
        b2 = self.gen_b2(step, arr)
        b3 = self.gen_b3(step, arr)

        # Compute slope (m) and intercept (b)
        m = ((a1 * b3) - (a2 * a3)) / ((a1 * b2) - (a2 * b1))
        b = (a3 / a1) - ((a2 / a1) * m)

        return [m, b]

    def gen_a2(self, step, arr):
        return sum(i * step for i in range(len(arr)))

    def gen_a3(self, arr):
        return sum(arr)

    def gen_b2(self, step, arr):
        return sum((i * step) ** 2 for i in range(len(arr)))

    def gen_b3(self, step, arr):
        return sum(arr[i] * (i * step) for i in range(len(arr)))


def parse_raw_temps(originalTemps: TextIO, step_size: int = 30) -> Generator[tuple[float, list[float]], None, None]:
    split = re.compile(r"[^0-9]*\s+|[^0-9]*$")

    for step, line in enumerate(originalTemps):
        yield (step * step_size), [
            float(input) for input in split.split(line) if len(input) > 0
        ]
