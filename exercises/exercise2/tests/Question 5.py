from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case
import pandas as pd
import numpy as np

OK_FORMAT = False
name = "Question 5"
points = 4


@test_case()
def test_billboard_songs(env):  
    billboard_songs  = env['Question5'].billboard_songs
    billboard_charts  = env['Question5'].billboard_charts

    assert_true(isinstance(billboard_songs, pd.DataFrame))
    assert_true(np.array_equal(np.unique(billboard_songs["track_id"]),np.unique(billboard_charts["track_id"])))
    assert_true(len(billboard_charts) == 24092)
    