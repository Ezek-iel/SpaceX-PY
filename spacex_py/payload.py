from ._helpers._api import _get

def get_payload_info(method = "", **query):
    """Gets information on SpaceX payloads.

    This function retrieves information on Space Exploration Technologies Corp
    payloads from the API.

    Returns
    -------
    dict
        A dictionary containing information on SpaceX payloads.

    Notes
    -----
    The returned dictionary has the following structure:
    {
        "payload_id": "string",
        "norad_id": "string",
        "reused": "boolean",
        "customers": ["string"],
        "nationality": "string",
        "manufacturer": "string",
        "payload_type": "string",
        "payload_mass_kg": "float",
        "payload_mass_lbs": "float",
        "orbit": "string",
        "orbit_params": {
            "reference_system": "string",
            "regime": "string",
            "longitude": "float",
            "semi_major_axis_km": "float",
            "eccentricity": "float",
            "periapsis_km": "float",
            "apoapsis_km": "float",
            "inclination_deg": "float",
            "period_min": "float",
            "lifespan_years": "float",
            "epoch": "string",
            "mean_motion": "float",
            "raan": "float",
            "arg_of_pericenter": "float",
            "mean_anomaly": "float"
        }
    }
    """
    return _get("payloads", method, query)
