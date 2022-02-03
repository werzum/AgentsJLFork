# Use Python 3

import timeit

for N in range(100, 500, 100):
  setup = f"""
gc.enable()
import os, sys
sys.path.insert(0, os.path.abspath("."))
from model import BoidFlockers
import random
random.seed(2)
model = BoidFlockers({N}, 100, 100, speed=1, vision=5, separation=4, cohere=0.25, separate=0.25, match=0.01)

def runthemodel(model):
  for i in range(100):
    model.step()
  """
  tt = timeit.Timer('runthemodel(model)', setup=setup)
  a = min(tt.repeat(20, 1))
  print(a)


