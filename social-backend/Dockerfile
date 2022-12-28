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

COPY ./backend .

RUN python3 manage.py collectstatic

# Update pip, wheel and setuptools to omit issues with package installation
# Update setuptools to address CVE-2022-40897 vulnerability
RUN pip3 install --no-cache-dir -U pip wheel setuptools

# Fixing issue with missing attrs package in pytest
# cffi package is needed for Argon2 dependency
# Cryptography is needed for using RSA algorithm in JWT
# six package is needed for django_behave
RUN pip3 install --no-cache-dir attrs cffi cryptography six
