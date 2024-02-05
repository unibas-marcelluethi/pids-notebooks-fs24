from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2c"
points = 3
@test_case()
def test_q2c(env):
    CI = env["Question2c"].CI

    assert_equal(len(CI), 2)
    assert_almost_equal(CI[1] - CI[0], 0.054 , places=2)
    assert_almost_equal(np.std(CI) , 0.027 , places=2)
    