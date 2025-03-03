#! /usr/bin/env python3

import sys

from parse_temps import parse_raw_temps
"""
Main function reads temps, sets up cores and their data along with time(s) and prints them
"""
def main():

    inTemps = sys.argv[1]

    with open(inTemps, "r") as temps_file:
        
        for tempNum in parse_raw_temps(temps_file):
            print(tempNum)

    with open(inTemps, "r") as temps_file:
        
        for tempNum in parse_raw_temps(temps_file):
            time, coreData = tempNum
            print(f"{time = } | {coreData = }")

    with open(inTemps, "r") as temps_file:
       
        times = []
        core0 = []
        core1 = []
        core2 = []
        core3 = []
        for time, coreData in parse_raw_temps(temps_file):
            times.append(time)
            core0.append(coreData[0])
            core1.append(coreData[1])
            core2.append(coreData[2])
            core3.append(coreData[3])

        print(f"{times[:4] = }")
        print(f"{core0[:4] = }")

        for time, *temps in list(
            zip(times, core0, core1, core2, core3)
        )[4:]:
            print(f"{time=} {temps=}")

    with open(inTemps, "r") as temps_file:
        
        times = []
        coreData = [[] for _ in range(0, 4)]

        for time, raw_coreData in parse_raw_temps(temps_file):
            times.append(time)

            for coreID, interpolation in enumerate(raw_coreData):
                coreData[coreID].append(interpolation)

        for time, *temps in list(zip(times, *coreData))[4:]:
            print(f"{time=} {temps=}")


if __name__ == "__main__":
    main()
