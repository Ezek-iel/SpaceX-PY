from spacex_py import starlink

def get_starlink_info():    
    got_starlink, _ = starlink.get_starlink_info()
    return got_starlink

def get_starlink_info_by_query():
    got_starlink, _ = starlink.get_starlink_info(version =  "v0.9",)
    return got_starlink

def test_get_starlink():
    assert type(get_starlink_info()) is list

def test_get_starlink_by_query():
    assert type(get_starlink_info_by_query()) is list