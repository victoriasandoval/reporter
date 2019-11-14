import datetime
import warnings
import json

auj = datetime.date.today()


def create_header(authors, destination):
    """"Returns the header string with authors listed
    
    Parametrs
    ---------
    authors: list of dict
        Each element of author should have the 
        'first' and 'last' keys
        
    Returns
    --------
    Header : str
         the header string at today's date
    
    """
    

    header_str=[
        f'{destination} le {auj.strftime("%A %d. %B %Y")}\n',
        '### auteurs\n',  
    ]

        
    for author in authors:
        _validate(author, key=('first', 'last'))
        first = author.get('first', "")
        
        try:
            last = author['last']
        except KeyError:
            warnings.warn("last key not found")
            last = ""
        
        header_str.append(f' - {first} {last}') 
    
    return "\n".join(header_str)


def _validate(author, key=('first', 'last')):
    missing = {'first', 'last'}.difference(author)
    if missing:
        print(f'missing key(s) {list(missing)} from dict')
        return False
    return True


def header_for_json(json_file, city):
    with open(json_file, 'r', encoding = 'utf-8') as file_handle:
        authors = json.load(file_handle) 
    return create_header(authors, city)