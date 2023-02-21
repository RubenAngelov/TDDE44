import sys
import common
import matplotlib
import matplotlib.pyplot as plt

def prepare_data2(data):
    x_values = []
    y_values = []
    for day in range(1, len(data[0])):
        total_cups = 0
        for hour in range(1, len(data)):
            total_cups += data[hour][day]

        x_values.append(data[0][day])
        y_values.append(total_cups)

    return [x_values, y_values]

def draw_diagram2(values, filename):
    print(values)
    # Line graph
    plt.figure()
    plt.plot(values[0], values[1])
    plt.ylabel("Antalet koppar")
    plt.savefig("{}_2_line.png".format(filename))

    # Bar graphe
    plt.figure()
    plt.bar(values[0], values[1])
    plt.ylabel("Antalet koppar")
    plt.savefig("{}_2_bar.png".format(filename))

def main():
    csv_data = common.load_csv(sys.argv[1])
    prepared_data = prepare_data2(csv_data)
    draw_diagram2(prepared_data, sys.argv[1][4:-4])

if __name__ == "__main__":
    main()