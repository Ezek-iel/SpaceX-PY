from spacex_py import dragons

def get_dragons():
    got_dragons, _ = dragons.get_dragon_info()
    return got_dragons

def get_dragons_by_query():
    got_dragons, _ = dragons.get_dragon_info(name = "Dragon 1")
    return got_dragons

def test_got_dragons():
    assert type(get_dragons()) is list

def test_got_dragons_by_query():
    assert type(get_dragons_by_query()) is list