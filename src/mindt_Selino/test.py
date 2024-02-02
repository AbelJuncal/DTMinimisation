from mindt_Selino.Resources.readInput import *
from mindt_Selino.Resources.intervalsGenerator import *
from mindt_Selino.quineMcCluskey import *
import sys

implicant = IntervalImplicant([(0,3), (2,4), (5,6)])
implicant2 = IntervalImplicant([(0,3), (2,4), (5,6)])

implicant3 = implicant.matches(implicant2)

print(implicant, implicant2, implicant3)