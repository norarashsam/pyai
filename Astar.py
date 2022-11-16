from simpleai.search import SearchProblem, astar

goal = 'HELLO WORLD'
class HelloProblem(SearchProblem):
    def actions(self, state):
        if len(state) < len(goal):
            return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        else:
            return []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == goal

    def heuristic(self, state):
        # how far are we from the goal?
        wrong = sum([1 if state[i] != goal[i] else 0
                    for i in range(len(state))])
        missing = len(goal) - len(state)
        return wrong + missing

problem = HelloProblem(initial_state='')
result = astar(problem)
print(result.state)
print(result.path())

