from spacex_py import launchpads

def get_launchpads():
    got_launchpads, _ = launchpads.get_launchpads()
    return got_launchpads

def test_get_launchpads():
    assert type(get_launchpads()) is list
