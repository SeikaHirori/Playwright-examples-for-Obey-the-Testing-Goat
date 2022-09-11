# Python Dockerfile



FROM python

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


RUN ["pytest","-n", "auto" , "-v", "--suppress-tests-failed-exit-code", "--continue-on-collection-errors","--junitxml=reports/results.xml"]

# Info on "--continue-on-collection-errors": https://stackoverflow.com/a/57003743
# "--suppress-tests-failed-exit-code" is from plugin: https://pypi.org/project/pytest-custom-exit-code/
    ## Ensures 'Results.xml' still gets published if collection error occurs


# Info about "tail": https://www.geeksforgeeks.org/tail-command-linux-examples/
CMD tail -f /dev/null