import sys
import common
import matplotlib
import matplotlib.pyplot as plt

def prepare_data1(data):
    x_values = []
    y_values = []
    for row in data[1:]:
        hour = row[0]
        average_this_hour = sum(row[1:]) / len(row[1:])
        x_values.append(hour)
        y_values.append(average_this_hour)

    return [x_values, y_values]

def draw_diagram1(values, filename):
    # Line graph
    plt.figure()
    plt.plot(values[0], values[1])
    plt.ylabel("Antalet koppar")
    plt.xlabel("Klockslag")
    plt.savefig("{}_1_line.png".format(filename))

    # Bar graph
    plt.figure()
    plt.bar(values[0], values[1])
    plt.ylabel("Antalet koppar")
    plt.xlabel("Klockslag")
    plt.savefig("{}_1_bar.png".format(filename))

def main():
    csv_data = common.load_csv(sys.argv[1])
    prepared_data = prepare_data1(csv_data)
    draw_diagram1(prepared_data, sys.argv[1][4:-4])

if __name__ == "__main__":
    main()