def write_inventory(filename, inventory):
    with open(filename, "w") as file:
        for item in sorted(inventory):
            file.write(f"{item}:{inventory[item]}\n")
