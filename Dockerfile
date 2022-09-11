# Python Dockerfile
## This template orignated from project miru


FROM alpine:latest

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN playwright install

RUN apt-get update && apt-get install libnss3.so\
    libnssutil3.so\
    libsmime3.so\
    libnspr4.so\
    libatk-1.0.so.0\
    libatk-bridge-2.0.so.0 \
    libcups.so.2\
    libdbus-1.so.3\
    libdrm.so.2\
    libxkbcommon.so.0\
    libXcomposite.so.1\
    libXdamage.so.1\
    libXfixes.so.3\
    libXrandr.so.2\
    libgbm.so.1\
    libasound.so.2\
    libatspi.so.0\
    libwayland-client.so.0

RUN ["pytest","-n", "auto" , "-v", "--suppress-tests-failed-exit-code", "--continue-on-collection-errors","--junitxml=reports/results.xml"]

# Info on "--continue-on-collection-errors": https://stackoverflow.com/a/57003743
# "--suppress-tests-failed-exit-code" is from plugin: https://pypi.org/project/pytest-custom-exit-code/
    ## Ensures 'Results.xml' still gets published if collection error occurs


# Info about "tail": https://www.geeksforgeeks.org/tail-command-linux-examples/
CMD tail -f /dev/null