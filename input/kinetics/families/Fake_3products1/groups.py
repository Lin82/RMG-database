#!/usr/bin/env python
# encoding: utf-8

name = "Fake_3products1/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["HOORRR"], products=["P1", "P2", "P3"], ownReverse=False)

reverse = "trimolecular"

recipe(actions=[
    ['GAIN_RADICAL', '*2', '1'],
    ['BREAK_BOND', '*2', 'S', '*3'],
    ['CHANGE_BOND', '*3', '1', '*4'],
    ['BREAK_BOND', '*4', 'S', '*5'],
    ['GAIN_RADICAL', '*5', '1'],
])


#entry(
#    index = 1,
#    label = "jOOQOOH",
#    group = "OR{jOOQ2OOH, jOOQ3OOH, jOOQ4OOH, jOOQ5OOH, jOOQ6OOH, jOOQ7OOH}",
#    kinetics = None,
#    reference = None,
#    referenceType = "",
#    shortDesc = u"""""",
#    longDesc = u"""""",
#    history = [
#        ("Thu Oct 10 2013","Victor Lambert <vrlambert@gmail.com","action","""Created to use only for importing other groups chemkin files"""),
#    ],
#)

entry(
    index = 1,
    label = "HOORRR",
    group = """
1 *1 H  0 {2,S}
2 *2 O  0 {1,S} {3,S}
3 *3 O  0 {2,S} {4,S}
4 *4 R  0 {3,S} {5,S}
5 *5 R  0 {4,S} {6,S}
6 *6 R  0 {5,S}
""",
    kinetics = None,
    reference = None,
    referenceType = "",
    shortDesc = u"""""",
    longDesc = u"""""",
    history = [
        ("Thu Dec 4 2014","Richard West","action","""Created to use only for importing other groups chemkin files"""),
    ],
)


tree(
"""
L1: HOORRR
"""
)