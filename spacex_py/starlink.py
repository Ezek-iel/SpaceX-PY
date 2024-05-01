from ._helpers._api import _get

def get_starlink_info(method="", **query):
    """Gets information on SpaceX Starlink.

    This function retrieves information on SpaceX Starlink from the API.

    Parameters
    ----------
    method : str, optional
        The HTTP method to use for the API request. Defaults to an empty string.
    **query : dict
        Additional query parameters to include in the API request.

    Returns
    -------
    dict
        A dictionary containing information on SpaceX Starlink.

    """
    return _get("starlink", method, query)