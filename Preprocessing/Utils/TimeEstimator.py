import sys
import time
import math
class TimeEstimator():

    def __init__(self, iteration_max, bar_length=20):
        self.get_time =  lambda: int(round(time.time() * 1000))
        self.start_time =  None
        self.time_log = []
        self.iteration_max = iteration_max
        self.bar_length = bar_length


    def start_timer(self):
        self.start_time = self.get_time()

    def tick(self):
        time_elapsed = self.get_time() - self.start_time
        self.time_log.append(time_elapsed)


    def estimate_remaining_time(self):
        avg_time_taken = math.fsum(self.time_log) / len(self.time_log)
        estimated_time_left = avg_time_taken * self.iteration_max
        return estimated_time_left / 60000


    def get_progressBar(self, value):
        percent = float(value) / self.iteration_max
        arrow = '-' * int(round(percent * self.bar_length) - 1) + '>'
        spaces = ' ' * (self.bar_length - len(arrow))
        sys.stdout.write("\rPercent: [{0}] Estimated Time: {1} {2}%".format(arrow + spaces, self.estimate_remaining_time(), int(round(percent * 100))))
        sys.stdout.flush()