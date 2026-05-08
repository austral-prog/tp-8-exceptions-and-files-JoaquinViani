def parse_log(filename):
    logs = {}

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if ":" not in line:
                raise ValueError("invalid log line")

            level, message = line.split(":", 1)

            level = level.strip()
            message = message.strip()

            if level not in logs:
                logs[level] = []

            logs[level].append(message)

    return logs
