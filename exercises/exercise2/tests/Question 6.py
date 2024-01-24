from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case
import pandas as pd
import numpy as np

OK_FORMAT = False
name = "Question 6"
points = 2

@test_case()
def test_billboard_songs(env):  
    name_song = env['Question6'].name_song
    assert_true(name_song == "It\'s Gonna Be Me")
