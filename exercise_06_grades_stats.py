def grades_stats(filename):
    result = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            student, grades_str = line.split(":")
            grades = grades_str.split(",")

            numbers = []

            for grade in grades:
                numbers.append(float(grade))

            average = sum(numbers) / len(numbers)
            maximum = max(numbers)
            minimum = min(numbers)

            result[student] = (average, maximum, minimum)

    return result
