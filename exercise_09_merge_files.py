def merge_files(file1, file2, output):
    with open(file1, "r") as f1:
        content1 = f1.read()

    with open(file2, "r") as f2:
        content2 = f2.read()

    with open(output, "w") as out:
        out.write(content1 + content2)
