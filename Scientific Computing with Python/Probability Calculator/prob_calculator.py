import copy
import random


# Consider using the modules imported above.

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for el in kwargs:
            self.contents.extend([el] * kwargs[el])

    def draw(self, num):
        if num >= len(self.contents):
            return self.contents
        else:
            result = []
            for i in range(num):
                result.append(self.contents.pop(random.randrange(0, len(self.contents))))
            return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ok_num = 0
    for i in range(num_experiments):
        balls = copy.deepcopy(hat)  # copy object reference use deepcopy
        drawn_balls = balls.draw(num_balls_drawn)
        if all(drawn_balls.count(el) >= expected_balls[el] for el in expected_balls):
            ok_num += 1
    return ok_num/num_experiments

