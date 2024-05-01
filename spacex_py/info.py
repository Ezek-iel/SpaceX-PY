from ._helpers._api import _get

def get_company_info():
    """Gets information on SpaceX

        Gets information on Space Exploration Technologies Corp
        from the API

    Returns
    -------
        dict
            a dict of the company information
    """
    return _get("company")

def get_company_history_info():
    """Gets company history and milestones

        Gets company history and milestones from
        the API

    Returns
    -------
        list
            a list of the company's historical events and milestones
    """
    return _get("history")

def get_roadster_info():
    """Gets information and orbital data for Starman Roadster.

    This function retrieves information and orbital data for the Starman Roadster
    from the SpaceX API. The API is updated every 10 minutes.

    Returns
    -------
    dict
        A dictionary containing the Starman Roadster's information and orbital data.

    """
    return _get("roadster")