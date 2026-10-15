from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


def heuristic(state=tuple, end=tuple)->int:
    return abs(state[0]- end[0]) + abs(state[1]-end[1])

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        frontier = PriorityQueueFrontier()
        frontier.add(root, root.cost + heuristic(root.state, grid.end))

        while not frontier.is_empty():
            nodo = frontier.pop()

            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)
            for action in grid.actions(nodo.state):
                successor_state = grid.result(nodo.state, action)
                successor_cost = nodo.cost + grid.individual_cost(nodo.state, action)

                if successor_state not in reached or successor_cost < reached[successor_state]:
                    son = Node(value="",
                               state=successor_state,
                               parent=nodo,
                               cost=successor_cost,
                               action=action)
                    reached[successor_state]=successor_cost
                    frontier.add(son, son.cost + heuristic(son.state, grid.end))
                                 
        return NoSolution(reached)
