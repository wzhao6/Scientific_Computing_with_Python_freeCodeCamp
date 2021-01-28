import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        ls = [[key]*value for key, value in kwargs.items()]
        self.contents = [item for sublist in ls for item in sublist]

    def draw(self, n):
        if n > len(self.contents):
            return self.contents
        else: 
            sample = random.sample(self.contents, n)
            for x in sample:
                self.contents.remove(x)
            return sample






def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_success = 0
    
    for _ in range(num_experiments):
        pool = copy.deepcopy(hat)
        result = pool.draw(num_balls_drawn)
        result_dict ={}
        unique_color = set(result)
        for x in unique_color:
            result_dict[x] = result.count(x)
        if result_dict.keys() >= expected_balls.keys():
            if all([result_dict[x]>=expected_balls[x] for x in expected_balls.keys()]):
                n_success +=1
    return n_success/num_experiments



