#! /usr/bin/env python3

import re
from typing import Generator, TextIO


def parse_raw_temps(
    originalTemps: TextIO, step_size: int = 30
) -> Generator[tuple[float, list[float]], None, None]:
    

    split = re.compile(r"[^0-9]*\s+|[^0-9]*$")

    for step, line in enumerate(originalTemps):
        yield (step * step_size), [
            float(input) for input in split.split(line) if len(input) > 0
        ]

def process_data(data):
    core_temps = {i: [] for i in range(4)}  

    for input in data:

        time = input[0]  
        temps = input[1] 
        for i, temp in enumerate(temps):
            core_temps[i].append((time, temp))  
            
    return [core_temps[i] for i in range(4)]