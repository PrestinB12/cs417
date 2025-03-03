# CS417 Piecewise Semester Project 
### By Prestin Bell

## Need to know
Language used: `Python`

Data used is in `Data Folder`

Sample Data is (including but not limited to) this:

 0 <= x <   30; 
 
 y =    80.0000 +     0.6333x; 
 
 interpolation 
 
 30 <= x <   60;

## Parameters, Returns, Functions used and why

### Within Main.py

 Reads data from the input file using the 'parse_temps' module.

    Parameters:
    inFile: Path for input file.

Returns:

    list: Temperature data.

    Open: Opening the input file

The write functon inters to the output file 'outFile'.

    Parameters used are:

    outFile (str): Path for output file.
    inters (list): List of tuples (these contain the output data)
    Open: opens the output file and allows it to be used (and defined)

Processes input data and write the results to the output files.

    Parameters used are (and why):

    inData: temperature data.
    inFile: path for input file.

### In Parse_Temps_Demo

This main function serves as the demomstration

### Parse_Temps.py
    This module is a collection of input helpers for the CPU Temperatures Project.

    All code may be used freely in the semester project, if and only if it is imported using
    ``import parse_temps`` or ``from parse_temps import {...}`` where ``{...}``
    represents one or more functions.

Take an input file and time-step size and parse all core temps.

    Args:
        original_temps: an input file

        step_size: time-step in seconds

    Yields:
        A tuple containing the next time step and a List containing n core
        temps as floating point values (where n is the number of cores)

### In Piecewise_Linear_Interpolation.py
Calculate piecewise linear interpolation parameters.

    Args:
    - data: A list of tuples for (x, y) data points.

    Returns:
    - list of tuples: List of tuples (x_k, x_k1, m, b) for  interpolating parts/segments