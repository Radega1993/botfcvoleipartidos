FROM python:3.7-alpine

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

COPY . /app
RUN make /app
CMD python /app/app.py
