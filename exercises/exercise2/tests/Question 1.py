from asserts import *
from otter.test_files import test_case
import numpy as np
OK_FORMAT = False
name = "Question 1"
points = 1

def get_population_melted(env):
  return env['Question1'].population_melted 

@test_case()
def test_year(env):  
  assert_equal(len(get_population_melted(env)['Year']), 16226)  

@test_case()
def test_country(env):
    assert_equal(len(get_population_melted(env)['Country Name']),16226)

@test_case()
def test_country_code(env):
    population_melted = get_population_melted(env)
    tmp = population_melted[(population_melted["Country Code"]=='ABW') & (population_melted["Year"]=='1965')]
    assert_equal(np.squeeze(tmp['Population'].values), 57357)

@test_case()
def test_country_name(env):
    population_melted = get_population_melted(env)
    assert_equal(population_melted.loc[(population_melted["Country Name"] == "Switzerland") & (population_melted["Year"] == "1960")]["Population"].values[0], 5327827.0)