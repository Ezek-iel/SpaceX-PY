from ._helpers._api import _get

def get_capsules(method=""):
    """Gets all capsules from the API.

    This function retrieves all capsules available from the SpaceX API.

    Parameters
    ----------
    method : str, optional
        The method used for the request.

    Returns
    -------
    list
        A list of capsules.

    """
    return _get("capsules", method)
