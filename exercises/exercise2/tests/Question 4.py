from asserts import *
from otter.test_files import test_case
import pandas as pd

OK_FORMAT = False
name = "Question 4"
points = 2


@test_case()
def test_height_melt(env):  
    height_melt = env['Question4'].height_melt    
    assert_true(isinstance(height_melt,pd.DataFrame))
    assert_true(len(height_melt[height_melt["Sex"] == "M"]) == len(height_melt[height_melt["Sex"] == "F"]))
    assert_true(height_melt.loc[(height_melt["Country Name"] == "Switzerland") & (height_melt["Sex"] == "F")]["Height in Cm"].values[0] == 164.33)

