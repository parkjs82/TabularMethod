import FindPI
import Optimization

# 입력 : damension,minterms
minterm = list(map(int,input().split()))
demension = minterm.pop(0)
pi = {}
key = FindPI.translate(pi, demension, minterm)
for i in range(0, demension):
    pi = FindPI.combine(pi, key)
    key = list(pi.keys())

EPIArray = {}
counter = 0
Optimization.showStep(pi, minterm, EPIArray)
while counter != len(pi):
    counter = len(pi)

    Optimization.findNEPI(pi, minterm, EPIArray)
    if len(minterm) == 0: break
    Optimization.rowDominance(pi, minterm, EPIArray)

    Optimization.findNEPI(pi, minterm, EPIArray)
    if len(minterm) == 0: break
    Optimization.columnDominance(pi, minterm, EPIArray)
