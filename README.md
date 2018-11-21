### A demo python package

## Installing with Pipenv

* Install from the Pipfile `pipenv install`
* Launch the Virtualenv `pipenv shell`

## Installing with Docker

* Build the image: `docker build -t reporter .`

**Warning:** Linux kernels 4.19.2 may have trouble building the image ([see issue](https://bbs.archlinux.org/viewtopic.php?id=241866)). The quickfix is `echo N | sudo tee /sys/module/overlay/parameters/metacopy` (tested on Arch 4.19.2)

* Run the container in interactive mode: `docker run -it -v $(pwd):/usr/reporter --rm reporter`
* Or in daemon mode: `docker run -d -v $(pwd):/usr/reporter reporter`

