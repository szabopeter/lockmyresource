FROM python:3 AS base

WORKDIR /src

COPY requirements_dev.txt requirements.txt
RUN pip install -r requirements.txt

COPY LICENSE  ./
COPY *.rst *.md *.gif ./
COPY Makefile MANIFEST.in setup.cfg setup.py tox.ini ./

COPY docs/ .
COPY tests ./
COPY lockmyresource ./

RUN flake8 lockmyresource tests
RUN python -m unittest discover .
RUN python setup.py bdist_wheel


FROM python:3 AS integration

COPY --from=base /src/dist/*.whl /whl/
WORKDIR /integration
COPY integration/requirements.txt ./
RUN pip install -r requirements.txt --no-index --find-links /whl/

COPY integration/*.py integration/*.sh ./
RUN ./run-all.sh
