import math

from tests import tests

test = tests()
test.testsUnitaires()
test.testWarshall([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])
test.testRoutage([[0,2,0,0],[0,0,3,0],[0,0,0,4],[0,0,0,0]])
#0 comme sommet de départ
test.testDijkstra([[0,2,5,4,math.inf,math.inf,math.inf],[2,0,2,math.inf,7,math.inf,math.inf],[5,2,0,1,4,3,math.inf],[4,math.inf,1,0,math.inf,4,math.inf],[math.inf,7,4,math.inf,0,1,5],[math.inf,math.inf,3,4,1,0,7],[math.inf,math.inf,math.inf,math.inf,5,7,0]],0)
#4 comme sommet de départ
test.testDijkstra([[0,2,5,4,math.inf,math.inf,math.inf],[2,0,2,math.inf,7,math.inf,math.inf],[5,2,0,1,4,3,math.inf],[4,math.inf,1,0,math.inf,4,math.inf],[math.inf,7,4,math.inf,0,1,5],[math.inf,math.inf,3,4,1,0,7],[math.inf,math.inf,math.inf,math.inf,5,7,0]],4)