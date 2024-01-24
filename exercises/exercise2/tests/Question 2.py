from nose.tools import assert_is_instance, assert_equal, assert_almost_equal, assert_true
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 2"
points = 1

@test_case()
def test_melted_sort(env):  
    population_melted_sort = env['Question2'].population_melted_sort 
    assert_true(sorted(list(population_melted_sort['Country Name'])) == list(population_melted_sort['Country Name']))
