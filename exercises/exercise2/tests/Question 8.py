OK_FORMAT = True

from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case
import pandas as pd
import numpy as np

OK_FORMAT = False
name = "Question 8"
points = 2

@test_case()
def test_talles_men(env):  
    country_largest_difference = env['Question8'].country_largest_difference
    largest_difference = env['Question8'].largest_difference
    assert_true(country_largest_difference == "Puerto Rico")
    assert_true(abs(largest_difference - 16.5) < 0.1)

