from spacex_py import payload

def get_payload_info():
    got_payloads, _ = payload.get_payload_info()
    return got_payloads

def get_payload_info_by_query():
    got_payloads, _ = payload.get_payload_info(norad_id=43205)
    return got_payloads

def test_get_payloads():
    assert type(get_payload_info()) is list

def test_get_payloads_by_query():
    assert type(get_payload_info_by_query()) is list