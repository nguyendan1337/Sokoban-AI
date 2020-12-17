from trial import Trial

Trial(file="../input/kask_input/sokoban03.txt",
      mode="kask",
      epsilon=0.8,
      discount_factor=0.9,
      learning_rate=0.9,
      r=5000,
      logging=False).run()
