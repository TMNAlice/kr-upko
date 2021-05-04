import heapq


class GraphWithWeights:
    def __init__(self, width=0, height=0, weights=None, walls=None):
        self.width = width
        self.height = height
        self.weights = weights or {}
        self.walls = walls or []

    class __PriorityQueue:
        def __init__(self):
            self.elements = []

        def empty(self):
            return len(self.elements) == 0

        def put(self, item, priority):
            heapq.heappush(self.elements, (priority, item))

        def get(self):
            return heapq.heappop(self.elements)[1]

    def __cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)

    def __in_bounds(self, coord):
        (x, y) = coord
        return 0 <= x < self.width and 0 <= y < self.height

    def __passable(self, node):
        return node not in self.walls

    def __neighbors(self, coord):
        (x, y) = coord
        results = [(x + 1, y), (x, y - 1), (x - 1, y), (x, y + 1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.__in_bounds, results)
        results = filter(self.__passable, results)
        return results

    def __differ(self, a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def a_star(self, start, goal):
        if self.width <= 0 or self.height <= 0:
            return "wrong size of graph"
        if not start or not goal:
            return "empty points"
        if not isinstance(start, tuple) or not isinstance(goal, tuple):
            return "wrong params"
        if list(filter(lambda p: p < 0, start + goal)):
            return "negative coordinates"
        if start[0] > self.height or goal[0] > self.height:
            return "wrong x coordinates"
        if start[1] > self.width or goal[1] > self.width:
            return "wrong y coordinates"
        if start in self.walls or goal in self.walls:
            return "teleported into wall"
        frontier = self.__PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        total_cost = {}
        came_from[start] = None
        total_cost[start] = 0
        while not frontier.empty():
            current = frontier.get()
            if current == goal:
                break
            for next_node in self.__neighbors(current):
                new_cost = total_cost[current] + \
                    self.__cost(current, next_node)
                if next_node not in total_cost or \
                        new_cost < total_cost[next_node]:
                    total_cost[next_node] = new_cost
                    priority = new_cost + self.__differ(goal, next_node)
                    frontier.put(next_node, priority)
                    came_from[next_node] = current
        current = goal
        path = [current]
        while current != start:
            if current not in came_from.keys():
                return "no way"
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


if __name__ == '__main__':
    weights = {(0, 0): 0, (0, 1): 3, (0, 2): 7, (0, 3): 4, (0, 4): 7,
               (0, 5): 2, (1, 0): 8, (1, 1): 9, (1, 2): 7, (1, 3): 2,
               (1, 4): 2, (1, 5): 9, (2, 0): 5, (2, 1): 7, (2, 2): 0,
               (2, 3): 0, (2, 4): 8, (2, 5): 6, (3, 0): 8, (3, 1): 6,
               (3, 2): 3, (3, 3): 3, (3, 4): 9, (3, 5): 1, (4, 0): 7,
               (4, 1): 8, (4, 2): 7, (4, 3): 6, (4, 4): 6, (4, 5): 7,
               (5, 0): 4, (5, 1): 3, (5, 2): 6, (5, 3): 7, (5, 4): 8,
               (5, 5): 2}
    walls = [(5, 2), (5, 3), (4, 1), (2, 0), (2, 3), (2, 2), (4, 4)]
    graph = GraphWithWeights(6, 6, weights, walls)
    path = graph.a_star((0, 0), (5, 4))
    print(path)
