# e_above_hull
Material: Energy above Hull, Phase Diagram

Developed by Jeffrey Hu, Jan 31, 2021. DFHS

[e_above_hull source code](e_above_hull.py)

[example input file](compound_energy.csv)

How to use: 

python3 e_above_hull_jfh.py compound_energy.csv 

A positive E above hull indicates that this material is unstable with respect to decomposition. A zero E above hull indicates that this is the most stable material at its composition.

```
if ehull < 1/1000:
        print "Entry is stable."
    elif ehull < 30/1000:
        print "Entry is metastable and could be stable at finite temperatures."
    elif ehull < 50/1000:
        print "Entry has a low probability of being stable."
    else:
        print "Entry is very unlikely to be stable."
```
