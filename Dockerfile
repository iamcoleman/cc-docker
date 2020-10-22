FROM python:3.8-alpine AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


# Utilize multi-stage build to help minimize the size of the image
FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apk update && apk add gcc

# Install python dependencies in /.venv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Set working directory to /home/app
WORKDIR /home/app

# Install application into container
COPY . .

# Run the executable
ENTRYPOINT ["python", "-m", "cc_docker_assignment"]
