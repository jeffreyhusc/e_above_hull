import sys

from pymatgen.ext.matproj import MPRester
from pymatgen.analysis.phase_diagram import *
from pymatgen.analysis.phase_diagram import PDPlotter


#e-hull calculation using pymatgen.  by Jianjun Hu
from pymatgen.analysis.phase_diagram import PhaseDiagram as PD
from pymatgen.analysis.phase_diagram import *
from pymatgen.core.composition import Composition

def e_above(formula, energy):


	#formula = 'Li6AsN'
	#energy = -27.53
	comp=Composition(formula)
	target = PDEntry(Composition(formula), energy)

	elements = list(comp.as_dict().keys())
	#print(elements)

	a = MPRester("API_KEY") #Go to materialsproject.org and create account to get API_KEY

	#Entries are the basic unit for thermodynamic and other analyses in pymatgen.
	#This gets all entries belonging to the Ca-C-O system.
	# entries = a.get_entries_in_chemsys(['Ca', 'C', 'O'])
	entries = a.get_entries_in_chemsys(elements)
	#print(entries)

	pd=PD(entries)

	# pd.get_decomposition(comp)

	ehull = pd.get_e_above_hull(target)

	#plotter = PDPlotter(pd)
	#plotter.show() 

	return ehull


file = sys.argv[1:]
with open(file[0], 'r') as fileobj:
	lines = fileobj.readlines()
	for x in lines[1:]:
		items = x.split(',')
		eabove = e_above(items[0], float(items[1]))
		print('ehull',items[0],eabove)
