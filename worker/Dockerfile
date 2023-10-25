## set the python version
ARG PYTHON_VERSION=3.10
ARG PYTHON_VERSION_MINOR=12

FROM python:${PYTHON_VERSION}.${PYTHON_VERSION_MINOR}-slim AS build-image

# install Poetry
RUN python -m pip install --no-cache-dir poetry==1.6.1

# use system python instead of virtualenv
# but in some use cases it is better to use poetry as venv builder and the copy created venv to the final image
RUN poetry config virtualenvs.create false

# set the working directory
WORKDIR /usr/src/workers

# install project dependencies
COPY poetry.lock pyproject.toml ./
RUN poetry install -E worker --no-root --no-cache --no-dev --no-interaction --no-ansi

# copy settings and supervisord config
COPY worker/supervisord.conf worker/settings.py ./

# copy the project
COPY backend ./backend

# Spawn workers according to config
ENTRYPOINT ["/bin/bash", "-c", "supervisord -c /usr/src/workers/supervisord.conf -n"]
