FROM python:3.11.1-slim-buster as build-stage

# C compiler is needed to build uwsgi package
RUN apt-get update && apt-get install -y gcc

RUN pip3 install --no-cache-dir -U pip wheel setuptools poetry

# Convert our dependencies from poetry to pip format
COPY pyproject.toml ./poetry.lock* /application/
WORKDIR /application

RUN poetry export -f requirements.txt --with test --without-hashes -o /tmp/requirements.txt

# Install python libraries
RUN pip3 install --no-cache-dir --user -r /tmp/requirements.txt

FROM python:3.11.1-slim-buster as run-stage

# Copy built Python dependencies from build-stage
COPY --from=build-stage /root/.local /root/.local

# Add scripts like uwsgi to path in order to be able to run it from a CLI
# It will add all executables from Python dependencies to PATH
ENV PATH="${PATH}:/root/.local/bin"

RUN mkdir -p /application
WORKDIR /application

COPY . .

RUN python3 manage.py collectstatic

# Fixing issue with missing attrs package in pytest
RUN pip install attrs

ENTRYPOINT ["uwsgi", "--ini", "/application/uwsgi.ini"]

# ToDo: run migrations