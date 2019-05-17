import datetime


def create_header(author_list, place="Paris"):
    """Returns the header text from authors list.

    Parameters
    ----------
    author_list : a list of dicts
        Each dictionnary should have "firstname"
        and "lastname" keys
    place : str, optional, default 'Paris'
        The place the report was edited


    Returns
    -------
    header : str
        The header string

    """
    ajd = datetime.date.today()

    lines = [f"{place}, le {ajd.strftime('%d/%m/%y')}\n", "## Authors\n"]
    for aut in author_list:

        firstname = aut.get("firstname", "")
        lastname = aut.get("lastname", "")
        lines.append(f"- {firstname} {lastname}")

    return "\n".join(lines)


def greet():
    """ A realy minimal function
    """
    print("Hello World!")
