# TabularMethod
Quine-McCluskey Method

Test Cases
---------------------
(입력의 개수) (minterms)
```
3 0 1 5 6 7

3 0 1 2 3 7

4 0 2 3 6 7 11 15

4 0 4 8 10 11 12 13 15

4 0 2 3 4 6 7 9 11 13 15

4 0 2 5 6 7 8 9 13 //petrick`s Method 구현필요
```
Algorithm
---------------------
### FindPI.py
---
1. translate\
계산의 효율과 가독성을 위해 a`,a 대신 0과 1을 사용한다.

2. combine\
`combineChech`의 반환값이 1일때 minterm을 더해 새로 만든 dictionary에 추가하며,\
combine함수의 반복문이 끝난 후 사용되지 않은 PI들또한 dictionary에 추가해 반환한다.

3. sort\
merge된 pi들의 순서를 오름차순 정리하기 위해 merge의 표현인 '-' 대신 2로 치환한다.

`main.py`실행 순서
```
import FindPI
minterm = list(map(int,input().split()))
demension = minterm.pop(0)
pi = {}
key = FindPI.translate(pi, demension, minterm)
for i in range(0, demension):
    pi = FindPI.combine(pi, key)
    key = list(pi.keys())
    
```
### Optimization.py
---
1. showStep\
`makeTable`,`printTable`함수로 유의미한 최적화가 일어났을 때 진행 상황을 보여준다.
2. findNEPI\
`findPI`, `delDontCareMinterm`, `changeAblePI` 함수를 사용해 최적화 과정의 실질적인 frame이다.
3. rowDominance, columnDominance\
`makeTable`함수로 만든 table을 기준으로 전수조사를 통해 축소 가능한 pi와 minterm을 찾는다.

`main.py`실행 순서
```
import Optimization
EPIArray = {}
counter = 0
Optimization.showStep(pi, minterm, EPIArray)
while counter != len(pi):
    counter = len(pi)

    Optimization.findNEPI(pi, minterm, EPIArray)
    if len(minterm) == 0:
        break
    Optimization.rowDominance(pi, minterm, EPIArray)

    Optimization.findNEPI(pi, minterm, EPIArray)
    if len(minterm) == 0:
        break
    Optimization.columnDominance(pi, minterm, EPIArray)

```
Output
---------------------
input : 3 0 1 5 6 7
```
[0, 1, 5, 6, 7]
[1, 1, 0, 0, 0]
[0, 1, 1, 0, 0]
[0, 0, 1, 0, 1]
[0, 0, 0, 1, 1]
PI :  {' 0 1 ': '00-', ' 1 5 ': '-01', ' 5 7 ': '1-1', ' 6 7 ': '11-'}
EPI :  {}

simplify table
[5]
[1]
[1]
PI :  {' 1 5 ': '-01', ' 5 7 ': '1-1'}
EPI :  {' 6 7 ': '11-', ' 0 1 ': '00-'}

changeable pi removed
[5]
[1]
PI :  {' 5 7 ': '1-1'}
EPI :  {' 6 7 ': '11-', ' 0 1 ': '00-'}

simplify table
End
EPI :  {' 6 7 ': '11-', ' 0 1 ': '00-', ' 5 7 ': '1-1'}

```

input : 4 0 4 8 10 11 12 13 15
```
[0, 4, 8, 10, 11, 12, 13, 15]
[1, 1, 1, 0, 0, 1, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 1, 1, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 0, 1, 1]
PI :  {' 0 4 8 12 ': '--00', ' 8 10 ': '10-0', ' 10 11 ': '101-', ' 11 15 ': '1-11', ' 12 13 ': '110-', ' 13 15 ': '11-1'}
EPI :  {}

simplify table
[10, 11, 13, 15]
[1, 0, 0, 0]
[1, 1, 0, 0]
[0, 1, 0, 1]
[0, 0, 1, 0]
[0, 0, 1, 1]
PI :  {' 8 10 ': '10-0', ' 10 11 ': '101-', ' 11 15 ': '1-11', ' 12 13 ': '110-', ' 13 15 ': '11-1'}
EPI :  {' 0 4 8 12 ': '--00'}

row dominance operated
[10, 11, 13, 15]
[1, 1, 0, 0]
[0, 1, 0, 1]
[0, 0, 1, 1]
PI :  {' 10 11 ': '101-', ' 11 15 ': '1-11', ' 13 15 ': '11-1'}
EPI :  {' 0 4 8 12 ': '--00'}

simplify table
End
EPI :  {' 0 4 8 12 ': '--00', ' 13 15 ': '11-1', ' 10 11 ': '101-'}

```

Limitation
---------------------
  4 0 2 5 6 7 8 9 13 
취의 예시처럼 Petrick`s Method가 필요한 테스트케이스에서 결괏값을 도출해내지 못한다.
