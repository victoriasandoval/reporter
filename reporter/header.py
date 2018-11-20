"""
Header creation utility

"""
import json
import sys
from datetime import date
from functools import wraps


def add_copyright(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        res = func(*args, **kwargs)
        res += '\n © humancoders 2018\n'
        return res
    return decorated

@add_copyright
def create_header(authors_json,
                  place='Paris',
                  **print_kwargs):

    """returns the header string

    Parameters
    ----------
    authors_json : path to a json file with authors info,
      a dictionnary of dictionnaries with the authors
      each entry should have a 'name' key
    place : str
      the place from which the report is created
    **print_kwargs : keyword arguments passed to the print function

    See Also
    --------
    print

    Returns
    -------
    header : str
       the header string

    Example
    -------

    >>> print(create_header(authors, 'Paris'))

    ### Paris, le 19 novembre 2018


    Auteurs:
        - John Lennon
        - Paul MacCartney
        - George Harisson
        - Ringo Star



    """
    with open(authors_json, 'r') as fp:
        authors = json.load(fp)

    ligne1 = f"### {place}, le {date.today().strftime('%d %B %Y')}"
    auteurs = """Auteurs:\n\t- """
    names = (val.get('name', '') for val in authors.values())
    auteurs = auteurs + '\n\t- '.join(names)
    res = '\n'.join([ligne1, auteurs])
    return res

if __name__ == '__main__':

    json_path = sys.argv[1]
    print(create_header(json_path))
