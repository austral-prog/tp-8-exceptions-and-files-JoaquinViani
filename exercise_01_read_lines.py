def read_lines(filename):
    result = []

    with open(filename, "r") as file:
        for line in file:
            clean = line.strip()

            if clean != "":
                result.append(clean)

    return result
