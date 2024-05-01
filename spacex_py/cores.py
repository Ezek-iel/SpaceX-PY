from ._helpers._api import _get

def get_cores(method="", **query):
    """Gets all core parts based on query strings

    This function retrieves all core parts from the SpaceX API
    based on the provided query strings.

    Parameters
    ----------
    method : str, optional
        The HTTP method used for the request. Defaults to an empty string.
    query : keyword arguments
        Additional query parameters to be included in the request.

    Returns
    -------
    list
        A list of core parts retrieved from the API.

    """
    return _get("cores", method, query)