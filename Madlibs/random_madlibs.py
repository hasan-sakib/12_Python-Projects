from Madlibs.sample_madlibs import goal
from Madlibs.sample_madlibs import intro
import random

if __name__=="__main__":
    m = random.choice([intro,goal])
    m.madlib()