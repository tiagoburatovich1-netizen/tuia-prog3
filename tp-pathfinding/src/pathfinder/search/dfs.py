from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # test objetivo
        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        # Initialize frontier with the root node
        frontier = StackFrontier()
        frontier.add(root)

        while not frontier.is_empty():
            # Extrae el próximo nodo de la pila
            node = frontier.remove()

            # Si el estado aún no ha sido expandido
            if node.state in expanded:
                continue
            expanded[node.state] = True
            
            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)

                # omite a los estados ya alcanzados
                if successor_state not in expanded:
                    # crea el nodo hijo
                    son = Node(
                        "",
                        successor_state,
                        cost=node.cost + grid.individual_cost(node.state, action),
                        parent=node,
                        action=action,
                    )
                    # test objetivo
                    if grid.objective_test(successor_state):
                        return Solution(son, expanded)

                    # agrega el hijo a la frontera
                    frontier.add(son)
                
        return NoSolution(expanded)
