def safe_average(filename):
    numbers = []

    with open(filename, "r") as file:
        for line in file:
            try:
                number = float(line.strip())
                numbers.append(number)
            except ValueError:
                pass

    if len(numbers) == 0:
        raise ValueError("no valid numbers")

    return sum(numbers) / len(numbers)
