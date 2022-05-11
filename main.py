import FindPI
import Optimization


minterm = [4,8, 0, 4, 8, 10, 11, 12, 13, 15]
demension = minterm.pop(0)
minterm.pop(0)
pi = {}
key = FindPI.translate(pi, demension, minterm)
for i in range(0, demension):
    pi = FindPI.combine(pi, key)
    key = list(pi.keys())

EPIArray = {}
counter = 0
Optimization.showStep(pi, minterm, EPIArray)
while (counter != len(pi)):
    counter = len(pi)
    Optimization.findNEPI(pi, minterm, EPIArray)
    if (len(minterm) == 0): break
    Optimization.rowDominance(pi, minterm, EPIArray)
    Optimization.columnDominance(pi, minterm, EPIArray)
