# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from mindt_Selino.Implicant.implicant import *

class BooleanImplicant(Implicant):
    def __init__(self, string):
        self.string = string

    def matches(self, otherImplicant):
    
        difference = 0
        merging = ""

        for z in range(len(self.string)):
            if self.string[z] == otherImplicant.string[z]:
                merging = merging + self.string[z]
            else:
                merging = merging + "-"
                difference+=1

        if(difference == 1):
            return BooleanImplicant(merging)
        
        return None

    def __str__ (self):
        return self.string