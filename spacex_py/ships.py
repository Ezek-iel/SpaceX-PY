from ._helpers._api import _get

def get_ship_info(method="", **query):
    """Gets information on SpaceX ships.

    This function retrieves information on Space Exploration Technologies Corp
    ships from the API.

    Parameters
    ----------
    method : str, optional
        The HTTP method to use for the API request. Default is an empty string.
    **query : dict
        Additional query parameters to include in the API request.

    Returns
    -------
    dict
        A dictionary containing information on SpaceX ships.

    """
    return _get("ships", method, query)