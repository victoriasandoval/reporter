### A demo python package

[![Build Status](https://travis-ci.org/glyg/reporter.svg?branch=master)](https://travis-ci.org/glyg/reporter) [![Coverage Status](https://coveralls.io/repos/github/glyg/reporter/badge.svg?branch=master)](https://coveralls.io/github/glyg/reporter?branch=master)
## Installing with Pipenv

* Install from the Pipfile `pipenv install`
* Launch the Virtualenv `pipenv shell`

## Installing with Docker

* Build the image: `docker build -t reporter .`

**Warning:** Linux kernels 4.19.2 may have trouble building the image ([see issue](https://bbs.archlinux.org/viewtopic.php?id=241866)). The quickfix is `echo N | sudo tee /sys/module/overlay/parameters/metacopy` (tested on Arch 4.19.2)

* Run the container in interactive mode: 
    - `docker run -it -v $(pwd):/usr/reporter -p 443:5000 --rm reporter`
    - inside the container: `FLASK_APP=reporter/api.py flask run --host=0.0.0.0`


* Or in daemon mode (HTTP): `docker run -d -v $(pwd):/usr/reporter -p 80:5000 reporter`
* Or in daemon mode (HTTPS): `docker run -d -v $(pwd):/usr/reporter -p 443:5000 reporter`

## testing

* RUN the tests:
    - with pytest: `py.test`
    - with pytest and coverage reporting (stdout + html): `coverage run -m py.test && coverage report && coverage html -d build/coverage`
    - reports will be in `build/coverage`
