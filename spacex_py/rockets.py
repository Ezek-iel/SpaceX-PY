from ._helpers._api import _get

def get_rockets(method=""):
    """Gets information related to SpaceX rockets.

    This function retrieves information related to SpaceX rockets from the API.

    Parameters
    ----------
    method : str, optional
        The method used for the request.

    Returns
    -------
    list
        A list of the rockets.

    """
    return _get("rockets", method)