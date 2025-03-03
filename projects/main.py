import parse_temps  
import piecewise_linear_interpolation  

def read_data(inFile):

    with open(inFile, 'r') as file:
        return list(parse_temps.parse_raw_temps(file))

def writeData(outFile, inters):
    with open(outFile, 'w') as f:
        for x_k, x_k1, m, b in inters:
            f.write(f"{x_k:10} <= x < {x_k1:4}; y = {b:10.4f} + {m:10.4f}x; interpolation\n")


def processData(inData, inFile):

    processed_data = parse_temps.process_data(inData)

    for i, core in enumerate(processed_data):
        inters = piecewise_linear_interpolation.calculate(core)
        name = inFile.rsplit('.', 1)[0]
        outFile = f"{name}-core-{i:02d}.txt"
        writeData(outFile, inters)

def main(inFile):
    
    data = read_data(inFile)
    processData(data, inFile)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
