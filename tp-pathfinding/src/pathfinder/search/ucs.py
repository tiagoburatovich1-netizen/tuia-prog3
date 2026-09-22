from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

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
        frontier.add(root, priority=root.cost)

        reached[root.state] = root.cost

        while not frontier.is_empty():
            # extrae el nodo con menor costo    
            node = frontier.pop()
            # test objetivo 
            if grid.objective_test(node.state):
                return Solution(node, reached)
            
            for action in grid.actions(node.state):
                successor_state = grid.result(node.state, action)
                successor_cost = node.cost + grid.individual_cost(node.state, action)

                if (successor_state not in reached or successor_cost < reached[successor_state]):
                    son = Node(
                        "",
                        successor_state,
                        cost=successor_cost,
                        parent=node,
                        action=action,
                    )
                    reached[successor_state] = son.cost
                    frontier.add(son)
        
        return NoSolution(reached)
