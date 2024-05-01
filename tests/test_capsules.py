from spacex_py import capsules

def get_capsules():
    got_capsules, _ = capsules.get_capsules()
    return got_capsules

def test_get_capsules():
    assert type(get_capsules()) is list
