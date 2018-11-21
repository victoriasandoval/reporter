# docker build -t reporter .
# docker run -it --rm reporter

FROM python:3.7

# install packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -q -y \
    bash \
    vim \
    curl \
    libhdf5-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/reporter

COPY ./ /usr/reporter
RUN pip install -r requirements_pip.txt

#CMD ["python", "./app.py"]
#CMD ["py.test", "-s", "./tests"]
CMD ["/bin/bash"]
