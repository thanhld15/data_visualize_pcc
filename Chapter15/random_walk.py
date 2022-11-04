from random import choice

def get_step():
    """Generate a random step for a walk"""
    
    direction = choice([-1,1])
    distance = choice([0,1,2,3,4,5,6,7,8])
    return direction * distance

class RandomWalk():
    """A class to generate a Random Walk"""

    def __init__(self, num_points = 5000):
        """Initialize the attributes to a walk"""
        self.num_points = num_points

        # Walk always start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """A function to generate all the points of random walk"""

        # Keep walking until reach the maximum number of points
        while(len(self.x_values) < self.num_points):
            # Choose direction and distance of the walk
            x_step = get_step()

            y_step = get_step()

            # Reject all meaningless walk
            if x_step == 0 and y_step == 0:
                continue

            # Find and update the next position after taking the walk
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)