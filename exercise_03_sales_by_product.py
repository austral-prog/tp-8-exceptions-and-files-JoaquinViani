def read_sales(filename):
    sales = {}

    with open(filename, "r") as file:
        content = file.read().strip()

    entries = content.split(";")

    for entry in entries:
        if entry == "":
            continue

        product, value = entry.split(":")
        value = float(value)

        if product not in sales:
            sales[product] = []

        sales[product].append(value)

    return sales


def process_sales(data):
    for product in data:
        total = sum(data[product])
        average = total / len(data[product])

        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")
