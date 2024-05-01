from spacex_py import rockets

def get_rockets():
    got_rockets, _ = rockets.get_rockets()
    return got_rockets

def test_get_rockets():
    assert type(get_rockets()) is list
