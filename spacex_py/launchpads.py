from ._helpers._api import _get

def get_launchpads(method=""):
    """
    Gets information related to launchpads used for SpaceX flights.

    This function retrieves information related to launchpads from the SpaceX API.

    Parameters
    ----------
    method : str, optional
        The method used for the request.

    Returns
    -------
    list
        A list of the launchpads.

    """
    return _get("launchpads", method)