def generate_table(table_type, size=10, **options):
    table = []

    if table_type == "multiplication":
        base = options.get("base", 1)
        for i in range(base, size + 1):
            row = []
            for j in range(base, size + 1):
                row.append(i * j)
            table.append(row)

    elif table_type == "addition":
        base = options.get("base", 1)
        for i in range(base, size + 1):
            row = []
            for j in range(base, size + 1):
                row.append(i + j)
            table.append(row)

    elif table_type == "power":
        exponent = options.get("exponent", 2)
        for i in range(1, size + 1):
            table.append(i ** exponent)

    return table



for row in generate_table("multiplication", size=5):
    print(row)

for row in generate_table("addition", size=3):
    print(row)

from pprint import pprint
pprint(generate_table("power", size=5, exponent=3))