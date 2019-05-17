from reporter.generator import create_header


def test_reporter():
    assert True


def test_generator():
    #pass
    authors = [{"firstname": "John", "lastname": "paul"},
               {"firstname": "Georges", "lastname": "paul"}]
    result = create_header(authors)
    # assert type(result) == str
    assert isinstance(result, str)
    assert "John" in result
