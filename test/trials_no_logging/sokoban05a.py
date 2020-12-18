from datetime import datetime

from parameterized import *

from output_format import output
from trial import Trial
from unittest import TestCase
from constants import TRAINING_EPISODES


class TestTrialNoLogging(TestCase):
    solution_length = {}
    episode_length = {}

    @parameterized.expand([
        # Varying the learning rate parameter:
        (0.8, 0.9, 0.9),
        (0.8, 0.9, 0.6),
        (0.8, 0.9, 0.3),
        # Discount factor parameter:
        (0.8, 0.9, 0.9),
        (0.8, 0.6, 0.9),
        (0.8, 0.3, 0.9),
        # Epsilon parameter:
        (0.8, 0.9, 0.9),
        (0.6, 0.9, 0.9),
        (0.3, 0.9, 0.9),
    ])
    def test_run_trial(self, epsilon, discount_factor, learning_rate):
        trial = Trial(file="../input/kask_input/sokoban05a.txt",
                      mode="kask",
                      epsilon=epsilon,
                      discount_factor=discount_factor,
                      learning_rate=learning_rate,
                      r=TRAINING_EPISODES,
                      logging=False)

        status, episode, explored = trial.run()

        print("Status = {s}".format(s=status))
        print("Episode = {e}".format(e=episode))
        print("Length of solution = {l}".format(l=len(explored)))
        output(explored)
        if status:
            self.__class__.solution_length[(epsilon, discount_factor, learning_rate)] = len(explored)
            self.__class__.episode_length[(epsilon, discount_factor, learning_rate)] = episode

        self.assertTrue(status, "Trial failed and found no solution.")

    def setUp(self):
        self.tick = datetime.now()

    def tearDown(self):
        self.tock = datetime.now()
        diff = self.tock - self.tick
        print("Trial time = {t}ms".format(t=(diff.microseconds / 1000))), "ms"

    @classmethod
    def tearDownClass(cls):
        print("--------------------")
        print("Printing Class data:")
        print("--------------------")

        params_with_min_solution_length = min(cls.solution_length, key=cls.solution_length.get)
        print("Params {p} had shortest solution of length: {m}".format(p=params_with_min_solution_length,
                                                                       m=cls.solution_length[
                                                                           params_with_min_solution_length]))

        params_with_min_episode_length = min(cls.episode_length, key=cls.episode_length.get)
        print("Params {p} had shortest number of episodes: {m}\n".format(p=params_with_min_episode_length,
                                                                         m=cls.episode_length[
                                                                             params_with_min_episode_length]))

        params_with_max_solution_length = max(cls.solution_length, key=cls.solution_length.get)
        print("Params {p} had longest solution of length: {m}".format(p=params_with_max_solution_length,
                                                                      m=cls.solution_length[
                                                                          params_with_max_solution_length]))

        params_with_max_episode_length = max(cls.episode_length, key=cls.episode_length.get)
        print("Params {p} had longest number of episodes: {m}\n".format(p=params_with_max_episode_length,
                                                                        m=cls.episode_length[
                                                                            params_with_max_episode_length]))

        print("Solution length data:")
        print(cls.solution_length)

        print("\nEpisode length data:")
        print(cls.episode_length)

# TODO add test that verifies solution is correct
