import datetime
import json
import tempfile
from reporter.header import create_header


def test_create_header():

    authors = {
        'auth1': {
            'name': 'John John',
            'email': 'john@example.com'
        },
        'auth2': {
            'name': 'Paul Paul',
        }
    }

    json_file = tempfile.mktemp(suffix='.json')
    with open(json_file, 'w') as fp:
        json.dump(authors, fp)

    place = 'Marseille'
    res = create_header(json_file, place)
    assert res.startswith('### Marseille')
    assert '- John John' in res

    res = create_header(json_file, 'Paris')
    assert res.startswith('### Paris')
