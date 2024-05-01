from ._helpers._api import _get

def get_dragon_info(methods = '', **query):
    """Gets information on SpaceX Dragon spacecraft.

    This function retrieves information on the SpaceX Dragon spacecraft
    from the SpaceX API.

    Returns
    -------
    dict
        A dictionary containing information on the SpaceX Dragon spacecraft.

        The dictionary has the following keys:
        - 'name': The name of the Dragon spacecraft.
        - 'type': The type of the Dragon spacecraft.
        - 'active': A boolean indicating whether the Dragon spacecraft is active.
        - 'crew_capacity': The maximum number of crew members the Dragon spacecraft can carry.
        - 'sidewall_angle_deg': The sidewall angle of the Dragon spacecraft in degrees.
        - 'diameter': The diameter of the Dragon spacecraft in meters.
        - 'heat_shield': Information about the heat shield of the Dragon spacecraft.
        - 'thrusters': Information about the thrusters of the Dragon spacecraft.
        - 'launch_payload_mass': The maximum payload mass the Dragon spacecraft can carry to orbit.
        - 'launch_payload_vol': The maximum payload volume the Dragon spacecraft can carry to orbit.
        - 'return_payload_mass': The maximum payload mass the Dragon spacecraft can return from orbit.
        - 'return_payload_vol': The maximum payload volume the Dragon spacecraft can return from orbit.
        - 'pressurized_capsule': Information about the pressurized capsule of the Dragon spacecraft.
        - 'trunk': Information about the trunk of the Dragon spacecraft.
        - 'height_w_trunk': The height of the Dragon spacecraft with trunk in meters.
        - 'flickr_images': A list of URLs to Flickr images of the Dragon spacecraft.

    Raises
    ------
    requests.exceptions.RequestException
        If an error occurs while making the API request.

    Returns
    -------
    dict
        A dictionary containing information on the SpaceX Dragon spacecraft.
    """
    return _get("dragons", methods, query)
