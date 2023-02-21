import common
import skapa_kaffediagram_1 as sk1
import skapa_kaffediagram_2 as sk2

import sys
import matplotlib
import matplotlib.pyplot as plt

def draw_diagram_3(all_values, names):
	plt.figure()
	
	for values, name in zip(all_values, names):
		plt.plot(values[0], values[1], label=name)

	plt.xlabel("Klockslag")
	plt.ylabel("Antalet koppar")
	plt.legend(loc="upper left", bbox_to_anchor=(1, 0, 1, 1))
	
	plt.savefig("kaffediagram_3.png", bbox_inches="tight")

def main():
	names = []
	all_values = []
	for arg in sys.argv[1:]:
	    csv_data = common.load_csv(arg)
	    all_values.append(sk1.prepare_data1(csv_data))
	    names.append(arg[4:-4])

	draw_diagram_3(all_values, names)

main()