FROM python:3.8-slim as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY ["./requirements.txt", "./requirements.txt"]
RUN pip install --root . --upgrade -r requirements.txt --no-warn-script-location

FROM base

COPY --from=builder /install /

WORKDIR /usr/src/app
COPY . /usr/src/app

# Needed for application to work with fly.io PaaS
EXPOSE 8080

CMD /bin/bash -c "python main.py"
