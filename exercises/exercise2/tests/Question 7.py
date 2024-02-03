from asserts import *
from otter.test_files import test_case
import pandas as pd
import numpy as np

OK_FORMAT = False
name = "Question 7"
points = 1

@test_case()
def test_talles_men(env):  
    country_tallest_men = env['Question7'].country_tallest_men
    height_tallest_men = env['Question7'].height_tallest_men

    assert_true(country_tallest_men == "Netherlands")
    assert_true(abs(height_tallest_men - 183.78) < 0.1)

