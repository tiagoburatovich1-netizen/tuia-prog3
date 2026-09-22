from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        # Initialize frontier with the root node
        frontier = QueueFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            node = frontier.remove()

            #test objetivo
            if grid.objective_test(node.state):
                return Solution(node, reached)

            #explora las posibles acciones
            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)

                #omite a los estados ya alcanzados
                if successor_state in reached:
                    continue
                #marca el sucesor como alcanzado
                reached[successor_state] = True

                #crea el nodo hijo
                son = Node(
                    "",
                    state=successor_state,
                    cost=node.cost + grid.individual_cost(node.state, action),
                    parent=node,
                    action=action,
                )

                #agrega el hijo a la frontera
                frontier.add(son)

        #no se encontro solucion
        return NoSolution(reached)
