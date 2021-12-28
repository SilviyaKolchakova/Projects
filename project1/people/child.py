class Child:
    def __init__(self, food_cost, *toys_cost):
        result = food_cost + sum(toys_cost)
        self.cost = result
