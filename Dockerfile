FROM alpine:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY _py_ /app/_py_
COPY bin /app/bin
COPY core /app/core
COPY log /app/log
COPY modules /app/modules
COPY install.py /app/install.py
COPY pxxtf.py /app/pxxtf.py
COPY uninstall.py /app/uninstall.py

RUN \
    apk add --no-cache python3 && \
    apk add --no-cache --virtual .build-deps gcc python3-dev &&\
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

CMD [ "python3", "./install.py" ]