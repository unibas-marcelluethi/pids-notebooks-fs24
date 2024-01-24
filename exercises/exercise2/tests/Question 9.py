OK_FORMAT = True

from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case
import pandas as pd
import numpy as np

OK_FORMAT = False
name = "Question 9"
points = 1

@test_case()
def test_corr(env):  
    corr_avg_heights = env['Question9'].corr_avg_heights
    assert_almost_equal(corr_avg_heights,0.9287870871294992)
