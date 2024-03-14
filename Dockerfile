ARG VIRTUAL_ENV=/opt/venv

FROM python:3.10-slim-buster as base

ENV PYTHONBUFFERED=1
RUN apt -y update && apt -y install curl

ARG VIRTUAL_ENV=/opt/venv
FROM base AS build
ARG VIRTUAL_ENV
RUN apt update && apt -y install git gcc zlib1g-dev libjpeg-dev libpq-dev python3-dev
RUN pip install virtualenv
RUN virtualenv ${VIRTUAL_ENV}

ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

RUN pip install --upgrade pip wheel

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM base as final
ARG VIRTUAL_ENV

RUN useradd -u 1000 app
RUN apt update && apt -y install gettext

WORKDIR /app
USER app

COPY --from=build --chown=1000:1000 ${VIRTUAL_ENV} ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"

COPY --chown=1000:1000 . .


EXPOSE 8000