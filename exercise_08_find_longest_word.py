def find_longest_word(filename):
    with open(filename, "r") as file:
        content = file.read()

    words = content.split()

    if len(words) == 0:
        raise ValueError("file has no words")

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
