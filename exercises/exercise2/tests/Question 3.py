from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_height_tidy(env):  
    height_tidy = env['Question3'].height_tidy 
    if 'Female Height in Ft' in height_tidy:
        assert_true(False) # fail
    