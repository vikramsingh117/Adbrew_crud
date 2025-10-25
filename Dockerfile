# set base image (host OS)
FROM python:3.8

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get -y update
RUN apt-get install -y curl nano wget nginx git

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# Ensure apt knows about the newly added yarn repo, then install Yarn
RUN apt-get -y update && apt-get install -y yarn

# Make sure pip/setuptools/wheel are available and up-to-date
# The official python image usually includes pip, but upgrade to a recent version
RUN python -m pip install --upgrade pip setuptools wheel


ENV ENV_TYPE staging
ENV MONGO_HOST mongo
ENV MONGO_PORT 27017
##########

ENV PYTHONPATH=$PYTHONPATH:/src/

# copy the dependencies file to the working directory
COPY src/requirements.txt .

# install dependencies
# (celery==5.0.5).
RUN pip install "pip<24.1" && pip install -r requirements.txt
