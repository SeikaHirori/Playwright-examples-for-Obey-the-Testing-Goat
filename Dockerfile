# Python Dockerfile
## This template orignated from project miru


FROM ubuntu:latest
RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /usr/src/app

COPY requirements.txt .
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install playwright
RUN playwright install
RUN playwright install-deps



# RUN ["pytest","-n", "auto" , "-v", "--suppress-tests-failed-exit-code", "--continue-on-collection-errors","--junitxml=reports/results.xml"]

# Info on "--continue-on-collection-errors": https://stackoverflow.com/a/57003743
# "--suppress-tests-failed-exit-code" is from plugin: https://pypi.org/project/pytest-custom-exit-code/
    ## Ensures 'Results.xml' still gets published if collection error occurs


# Info about "tail": https://www.geeksforgeeks.org/tail-command-linux-examples/
CMD tail -f /dev/null