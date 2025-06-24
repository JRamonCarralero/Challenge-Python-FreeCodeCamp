import copy
import random

class Hat:

    def __init__(self, **kwargs):
        """
        Initializes a Hat instance with a dictionary of ball colors and their respective counts.

        Parameters:
            **kwargs: A dictionary where the keys are the ball colors and the values are the counts of each color.

        The instance variable 'contents' is a list of ball colors, and 'initial_balls_dict' is a dictionary of ball colors and counts that represents the initial state of the hat.
        """
        self.contents = []
        self.initial_balls_dict = kwargs

        for color, count in kwargs.items():
            self.contents.extend([color] * count)
    
    def draw(self, num_balls):
        """
        Draws a specified number of balls from the hat and returns them as a list.

        If the number of balls to draw is greater than or equal to the number of balls in the hat, the method returns all the balls in the hat and clears the hat.

        Parameters:
            num_balls (int): The number of balls to draw.

        Returns:
            list: A list of the drawn balls.
        """
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents.clear()
            return drawn_balls
        else:
            drawn_balls = []
            for _ in range(num_balls):
                index = random.randrange(len(self.contents))
                drawn_balls.append(self.contents.pop(index))
            return drawn_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Conducts an experiment to determine the probability of drawing a specific
    configuration of balls from a hat.

    The experiment involves drawing a specified number of balls from the hat
    multiple times and calculating the probability of drawing at least the 
    expected number of each specified ball color.

    Parameters:
        hat (Hat): An instance of the Hat class representing the initial state
            of the hat with balls.
        expected_balls (dict): A dictionary where keys are ball colors and
            values are the minimum number of each color expected to be drawn.
        num_balls_drawn (int): The number of balls to draw from the hat in each
            experiment.
        num_experiments (int): The number of times the experiment is conducted.

    Returns:
        float: The probability of drawing the expected configuration of balls
        at least once in the specified number of experiments.
    """
    many_times = 0

    for _ in range(num_experiments):
        temp_hat = Hat(**hat.initial_balls_dict)

        drawn_balls = temp_hat.draw(num_balls_drawn)

        drawn_balls_counts = {}
        for ball in drawn_balls:
            drawn_balls_counts[ball] = drawn_balls_counts.get(ball, 0) + 1

        successful = True
        for color, count in expected_balls.items():
            if drawn_balls_counts.get(color, 0) < count:
                successful = False
                break

        if successful:
            many_times += 1

    prob = many_times / num_experiments

    return prob


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)

print(probability)