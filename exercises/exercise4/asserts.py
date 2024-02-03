
def assert_equal(expected, actual):
    assert expected == actual,  f"{actual} does not equal {expected}"
    
def assert_almost_equal(expected, actual, places = 2):
    assert abs(expected - actual) < float(f"1e-{places}"), f"{actual} does not equal {expected} for given precision 1e-{places}"

def assert_is_instance(value, tpe):
    assert (isinstance(value, tpe)), f"{value} is not instance of {tpe}"

def assert_true(expr):
    assert(expr), f"{expr} does not evaluate to True"