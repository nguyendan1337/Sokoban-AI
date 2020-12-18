#################
# MAIN FUNCTION #
#################

# Complete for problems 0, 1, 2, 3, 4, 5a, 5b, 6a, 6b, 6c, 7a
from trial import Trial

Trial(file="../input/kask_input/sokoban07a.txt",
      mode="kask",
      epsilon=0.8,
      discount_factor=0.9,
      learning_rate=0.9,
      r=5000,
      logging=False).run()
