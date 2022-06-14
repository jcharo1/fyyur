FROM python:stretch


COPY . /app
WORKDIR /app

ARG PASS
ENV PASS=${PASS}

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


ENTRYPOINT ["gunicorn", "-b", ":80", "app:app"] 