from spacex_py import ships

def get_ships():
    got_ships, _ = ships.get_ship_info()
    return got_ships

def get_ships_by_query():
    got_ships, _ = ships.get_ship_info(ship_id="AMERICANCHAMPION")
    return got_ships

def test_get_ships():
    assert type(get_ships()) is list

def test_get_ships_by_query():
    assert type(get_ships_by_query()) is list
