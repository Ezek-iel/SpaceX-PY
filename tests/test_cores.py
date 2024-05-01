from spacex_py import cores

def get_cores():
    got_cores, _ = cores.get_cores()
    return got_cores

def get_cores_by_query():
    got_cores, _ = cores.get_cores(core_serial="B1050")
    return got_cores

def test_get_cores():
    assert type(get_cores()) is list 

def test_get_cores_by_query():
    assert type(get_cores_by_query()) is list