def load_csv(filename):
    with open(filename, "r") as f:
        data = []
        for line in f.readlines():
            row_elements = line.split(";")

            for i in range(len(row_elements)):
                try:
                    row_elements[i] = int(row_elements[i])
                except ValueError:
                    continue

            data.append(row_elements)

        return data