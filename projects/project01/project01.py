
def parse_line():
    ...

def read_file(file_name):
    """
    Takes in file name string argument, then opens and reads line by line,
    passing line to parsing function to increment count of rare-variant associated
    diseases in given file.

    Args:
        file_name (str): filepath for vcf file to be parsed

    Returns:
        dict: Dictionary containing count of disease frequencies
    """
    disease_count = dict()

    with open(file_name, mode='r', encoding='utf-8') as infile:
        for line in infile:
            clean_line = line.rstrip()

            # Skip information and header lines
            if clean_line[0] == "#":
                continue

            disease_parse = parse_line(line)

            # If parse_line returns one or more disease
            if len(disease_parse) >= 1:
                for disease in disease_parse:
                    if disease in disease_count:
                        disease_count[disease] += 1
                    else:
                        disease_count[disease] = 1

    return disease_count
            
            