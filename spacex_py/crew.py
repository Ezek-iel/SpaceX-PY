from ._helpers._api import _get

def get_crew_info(method = "", **query):
    """Gets information on SpaceX crew members.

    This function retrieves information on the crew members of SpaceX
    from the SpaceX API.

    Returns
    -------
    dict
        A dictionary containing information about the crew members. Each crew member
        is represented as a dictionary with the following keys:
        
        - 'name': The name of the crew member.
        - 'agency': The agency or organization the crew member belongs to.
        - 'status': The current status of the crew member.
        - 'image': The URL of the image representing the crew member.
        - 'wikipedia': The URL of the Wikipedia page for the crew member.
        - 'launches': A list of launch IDs associated with the crew member.

    Raises
    ------
    requests.exceptions.RequestException
        If there is an error while making the API request.

    Returns
    -------
    dict
        A dictionary containing information about the crew members.

    Examples
    --------
    >>> crew_info = get_crew_info()
    >>> print(crew_info['name'])
    'Elon Musk'
    >>> print(crew_info['agency'])
    'SpaceX'
    >>> print(crew_info['status'])
    'active'
    """

    return _get("crew", method, query)
