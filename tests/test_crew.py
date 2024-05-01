from spacex_py import crew

def get_crew():
    got_crew, _ = crew.get_crew_info()
    return got_crew

def get_cores_by_query():
    got_cores, _ = crew.get_crew_info(name = "Anna Kikina")
    return got_cores

def test_got_crew():
    assert type(get_crew()) is list

def test_got_crew_by_query():
    assert type(get_cores_by_query()) is list
