import parse_temps  
import piecewise_linear_interpolation  

"""
First read the data
"""

def readData(inFile):

    with open(inFile, 't') as file:

        return list(parse_temps.parse_raw_temps(file)) # Path for data 

"""
Then process the data
"""
def processData(inData, inFile):

    processed_data = parse_temps.process_data(inData)

    for i, core in enumerate(processed_data):

        inters = piecewise_linear_interpolation.calculate(core) #enter the data found/process and create output File 'outFile.txt'
        name = inFile.rsplit('.', 1)[0]
        outFile = f"{name}-core-{i:02d}.txt"
        writeData(outFile, inters)

"""
Then write the data to the output File
"""

def writeData(outFile, inters):

    with open(outFile, 'w') as f:
        for x_k, x_k1, m, b in inters:
            f.write(f"{x_k:10} <= x < {x_k1:4}; y = {b:10.4f} + {m:10.4f}x; interpolation\n")   # data outputted

"""
Main function
"""

def main(inFile):
    # calling functions in main
    data = readData(inFile)
    processData(data, inFile)

"""
Found following function off of stack overFlow
Link: https://stackoverflow.com/questions/23000075/purpose-of-if-name-main

Not sure if needed, 
it just The code checks if the script is being run directly 
and then passes the first command-line argument 
(sys.argv[1]) to the main function for processing. 
The sys module is used to access these arguments.
"""

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
