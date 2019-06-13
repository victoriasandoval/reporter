def greet():
    """ A realy minimal function
    """
    print("Hello World!")


import datetime
import warnings

def create_header(authors_list, location="Paris"):
    """Creates the document header with authors and date
    
    Parameters
    ----------
    authors_list : list of dict
        each dictionnary should have 'fisrtname' and 'lastname' keys
    location : str, optional, default 'Paris' 
        the place from which the report is edited
        
    Return
    ------
    header_text : str
        the text header
    ...
    """
    
    ajd = datetime.date.today().strftime('%d/%m/%y')

    texts = [f"{location}, le {ajd}\n\n", "#### Auteurs"]
    for person in authors_list:
        try:
            first = person["firstname"]
        except KeyError:
            warnings.warn('Missing firstname in author')
            first = ""
        try:    
            last = person["lastname"]
        except KeyError:
            warnings.warn('Missing lastname in author')
            last = ""
        finally:
            print("I'm always executed !")
        
        texts.append(f"- {first} {last}")
    
    return "\n".join(texts)
