def csv_to_dict(filename):
    result = []

    with open(filename, "r") as file:
        lines = file.readlines()

    if len(lines) <= 1:
        return []

    headers = lines[0].strip().split(",")

    for line in lines[1:]:
        line = line.strip()

        if line == "":
            continue

        values = line.split(",")

        person = {
            headers[0]: values[0],
            headers[1]: int(values[1]),
            headers[2]: values[2]
        }

        result.append(person)

    return result
