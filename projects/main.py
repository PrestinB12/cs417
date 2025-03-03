import parse_temps  
import piecewise_linear_interpolation  

def read_data(input_file):
    """
    Read data from the input file using the parse_temps module.

    Parameters:
    input_file: Path to the input file.

    Returns:
    list: List of parsed temperature data.
    """
    with open(input_file, 'r') as file:
        return list(parse_temps.parse_raw_temps(file))

def write_interpolations(output_file, interpolations):
    """
    Write interpolations to the output file.

    Parameters:
    output_file (str): Path to the output file.
    interpolations (list): List of tuples containing interpolation data.
    """
    with open(output_file, 'w') as f:
        for x_k, x_k1, m, b in interpolations:
            f.write(f"{x_k:10} <= x < {x_k1:4}; y = {b:10.4f} + {m:10.4f}x; interpolation\n")


def process_and_interpolate(input_data, input_file):
    """
    Process input data, perform interpolation, and write results to files.

    Parameters:
    input_data: List of input temperature data.
    input_file: Path to the input file.
    """
    processed_data = parse_temps.process_data(input_data)

    for i, core in enumerate(processed_data):
        interpolations = piecewise_linear_interpolation.calculate(core)
        base_name = input_file.rsplit('.', 1)[0]
        output_file = f"{base_name}-core-{i:02d}.txt"
        write_interpolations(output_file, interpolations)

def main(input_file):
    """
    Main function.

    Parameters:
    input_file: Path to the input file.
    """
    data = read_data(input_file)
    process_and_interpolate(data, input_file)

if __name__ == "__main__":
    import sys
    main(sys.argv[1])
