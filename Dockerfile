FROM python:3.11

# image maintainer
LABEL maintainer="Icaro Zelioli"

# defines the working directory
WORKDIR /

# copy the requirements file into the container
# and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# create the api folder and use it for volume mounting
RUN mkdir /personal_wiki
VOLUME /personal_wiki

# expose the port for the API
EXPOSE 5001