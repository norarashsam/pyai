from __future__ import print_function
from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, LEAST_CONSTRAINING_VALUE
variables = ('WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T')
domains = dict((v, ['red', 'green', 'blue']) for v in variables)
def cd(variables, values):
    return values[0] != values[1]  # expect the value of the neighbors to be different
constraints = [
    (('WA', 'NT'), cd),
    (('WA', 'SA'), cd),
    (('SA', 'NT'), cd),
    (('SA', 'Q'), cd),
    (('NT', 'Q'), cd),
    (('SA', 'NSW'), cd),
    (('Q', 'NSW'), cd),
    (('SA', 'V'), cd),
    (('NSW', 'V'), cd),
]
mp = CspProblem(variables, domains, constraints)
print(backtrack(mp))
print(backtrack(mp, variable_heuristic=MOST_CONSTRAINED_VARIABLE))
print(backtrack(mp, variable_heuristic=HIGHEST_DEGREE_VARIABLE))
print(backtrack(mp, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(mp, variable_heuristic=MOST_CONSTRAINED_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(backtrack(mp, variable_heuristic=HIGHEST_DEGREE_VARIABLE, value_heuristic=LEAST_CONSTRAINING_VALUE))
print(min_conflicts(mp))

