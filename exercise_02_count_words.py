def count_words(filename):
    counts = {}

    with open(filename, "r") as file:
        for line in file:
            words = line.lower().split()

            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1

    return counts
